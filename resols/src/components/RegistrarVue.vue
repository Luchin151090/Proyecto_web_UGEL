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
              Nueva resolución
            </v-btn>
          </template>
          <v-card class="blank" height="500">
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.nproyecto"
                      label="N° Proyecto"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.concepto"
                      label="Concepto"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.descripcion"
                      label="Descripcion"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.monto"
                      label="Monto (S/.)"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.distrito"
                      label="Distrito"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.Femision"
                      placeholder="DD/MM/AAAA"
                      label="Fecha emision"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.Fnotificacion"
                      label="Fecha notificacion"
                      placeholder="DD/MM/AAAA"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <form enctype="multipart/form-data" @submit.prevent="submit">
                    <v-file-input
                      v-model="file"
                      
                      accept="application/pdf"
                      label="PDF"
                      prepend-icon="mdi-file"
                    ></v-file-input>
                    </form>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" type="submit" text @click="save"> Save </v-btn>
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
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
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
      { text: "N° Proyecto", value: "nproyecto" },
      { text: "Concepto", value: "concepto" },
      { text: "Descripcion", value: "descripcion" },
      { text: "Monto", value: "monto" },
      { text: "Distrito", value: "distrito", sortable: false },
      { text: "F.Emision", value: "Femision" },
      { text: "F.Notificacion", value: "Fnotificacion" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    file:null,
    rules: [
      (value) => !value || value.size < 2000000 || "Archivos menos a 2 MB!",
    ],

    /*items: almacena la data del query*/
    items: [],
    config_request: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    config_header: {
      "Content-Type": "multipart/form-data",
    },
    editedIndex: -1,
    editedItem: {
      nproyecto: "",
      concepto: "",
      descripcion: "",
      monto: 0.0,
      distrito: "",
      Femision: "",
      Fnotificacion: "",
      tipo_id: 1,
    },
    defaultItem: {
      nproyecto: "",
      concepto: "",
      descripcion: "",
      monto: 0.0,
      distrito: "",
      Femision: "",
      Fnotificacion: "",
      tipo_id: 1,
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
    this.initialize();
  },

  methods: {
    async initialize() {
      axios
        .get("http://127.0.0.1:5000/resolucion/", this.config_request)
        .then((res) => {
          this.items = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editItem(item) {
      
      this.editedIndex = item.id; /*this.items.indexOf(item);*/


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

    async save() {
      
        /* cuando hay un registro existente lo editamos*/
        if(this.editedIndex>-1){
          console.log("id orig",this.editedIndex);
          let objeto = Object.assign(this.items[this.editedIndex], this.editedItem);
          let id = this.editedIndex;
          console.log(" id ",id);

          /* file */
          const formdata = new FormData();
          formdata.append("file",this.file);
         
       

          axios
          .put("http://127.0.0.1:5000/update/resolucion/"+id.toString(),
          objeto,
          this.config_request)
          .then((res)=>{})
          .catch((error)=>{
            console.log(error);
          })

          axios
        .post("http://127.0.0.1:5000/upload_file/"+id.toString(), formdata, this.config_header)
        .then((res) => {
          res.data.files;
          res.status;
          console.log(res.data.files);
        })
        .catch((error) => {
          console.log(error);
        });

        }

        /* si no lo creamos */
        else{
        console.log("pusheamos dato nuevo");
        console.log("DATO PUSHEAR",this.editedItem);
        axios
          .post(
            "http://127.0.0.1:5000/create/resolucion",
            this.editedItem,
            this.config_request
          )
          .then((res) => {})
          .catch((error) => {
            console.log(error);
          });

        
      }
      this.close();
    },
  },
};
</script>
