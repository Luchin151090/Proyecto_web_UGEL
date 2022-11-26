<template>
    <v-data-table
    :headers="headers"
    :items="items"
    :items-per-page="5"
    sort-by="calories"
    class="elevation-1 ma-6 grey darken-2 white--text"
    width="2000px"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Mi Resolución</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="grey darken-3"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Nueva Usuario
            </v-btn>
          </template>
          <v-card class="cyan">
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.nombre"
                      label="Nombres"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.apellido"
                      label="Apellidos"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.dni"
                      label="DNI"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.direccion"
                      label="Direccion"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="nick"
                      label="Usuario"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="email"
                      label="Email"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="password"
                      label="Contraseña"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                    v-model="rol"
                    :items="roles"
                    label="Rol de usuario"
                    ></v-select>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">
                Cancel
              </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this item?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)">
        mdi-pencil
      </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize"> Reset </v-btn>
    </template>
  </v-data-table>
</template>
<script>
    import axios from "axios";

export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,

    /*Cabecera de la tabla*/
    headers: [
      {
        text: "N° ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Usuario", value: "nickname" },
      { text: "Email Usuario", value: "email_usuario" },
      { text: "Nombres", value: "nombres" },
      { text: "Apellidos", value: "apellidos" },
  
    ],

    /*items: almacena la data del query*/
    items: [],
    config_request: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    editedIndex: -1,
    /* roles de usuario */
    rol:2,
    roles:[
        1,2
    ],


    /* usuario */
    password:"",
    nick:"",
    email:"",
  /* persona */
    editedItem: {
      nombre:"",
      apellido:"",
      dni:"",
      direccion:""
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
  }),

  computed: {
    formTitle() {
      console.log("Dentro de new FORMTITLE");
      return this.editedIndex === -1 ? "Nuevo documento" : "Editar Documento";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  created() {
    this.randomuser();
    this.randompass();
    this.initialize();
  },

  methods: {
    /* usuario - password */
    async randomuser(){
        var result = '';
        var chars='abcdefghijklmnopqrstuvwxyz0123456789';
    for (var i = 6; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)];

        this.nick= result;
        
    },/* ...continue...*/
    async randompass(){
        var result = '';
        var chars='ABCDEFGHIJKLMNÑOPQURSTUVWXYZ+-/*0123456789';
    for (var i = 6; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)];

        this.password= result;
        
    },
    
    /* data de usuarios */  
    async initialize() {
      axios
        .get("http://127.0.0.1:5000/usuarios_control", this.config_request)
        .then((res) => {
          this.items = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editItem(item) {
      console.log("Dentro de editItem: ", item);
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.items.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    async create_rol(){
        axios
          .post("http://127.0.0.1:5000/create/rol_user",{
            rol_id:this.rol
          },this.config_request)
          .then((res)=>{})
          .catch((error)=>{
            console.log(error);
          })
    },
    async create_user(){
        axios
          .post("http://127.0.0.1:5000/create/user",{
            nickname:this.nick,
            contraseña:this.password,
            email_user:this.email
          },this.config_request)
          .then((res)=>{
            this.create_rol();
          })
          .catch((error)=>{
            console.log(error);
          });
    },
  
    async save() {
      console.log("SAVE...");
      if (this.editedIndex > -1) {
        Object.assign(this.items[this.editedIndex], this.editedItem);
      } else {
        console.log("pusheamos dato nuevo");
        axios
          .post(
            "http://127.0.0.1:5000/create/person",
            this.editedItem,
            this.config_request
          )
          .then((res) => {
            this.create_user();
          })
          .catch((error) => {
            console.log(error);
          });
       

        

      }
      this.close();
    },
  },
};
</script>


<style>
    .fondito{
        background: url("https://media.istockphoto.com/vectors/books-sketch-seamless-vector-id594484448?k=20&m=594484448&s=612x612&w=0&h=6lvNgspQuiOQUidxaH7LPfiE7RcicUgwReKe-WEhSNc=");
    }
</style>