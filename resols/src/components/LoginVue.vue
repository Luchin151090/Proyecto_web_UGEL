<template>
  <v-app>
    <v-main class="fondo3">
      <v-card class="ma-auto mt-10" height="620" width="374">
        <v-img
          height="30%"
          src="https://thumbs.dreamstime.com/b/plaza-de-armas-arequipa-per%C3%BA-49441219.jpg"
        ></v-img>
        <v-card-title class="mt-0 mb-0 justify-center">
          Ugel-BuResol v1.0
        </v-card-title>
        <v-card-title class="amber--text justify-center">Login</v-card-title>

        <v-form
          class="mt-0 ml-5 mr-5"
          ref="forms"
          v-model="valid"
          lazy-validation
        >
          <v-text-field v-model="nombre" label="Usuario"></v-text-field>
          <v-text-field
            v-model="contrasena"
            label="Contraseña"
            type="password"
          ></v-text-field>

          <v-btn
            :disabled="!valid"
            color="amber"
            block
            class="white--text"
            @click="acceder"
          >
            Acceder
          </v-btn>

          <v-divider class="my-2"></v-divider>

          <v-btn block color="gray" class="mr-4" @click="registrar"
            >Registrarse</v-btn
          >
          <v-divider class="my-2"></v-divider>
          <v-btn block color="blue" class="white--text" @click="olvidar"
            >¿Olvidaste Contraseña?</v-btn
          >
        </v-form>
      </v-card>
    </v-main>
  </v-app>
</template>
<script>
import axios from "axios";
export default {
  data: () => ({
    /*cabecera de control*/
    config_request: {
      "Content-Type": "application",
      "Access-Control-Allow-Origin": "*",
    },
    events:['click','mousemove','mousedown','scroll','keypress','load'],

    /*v- models*/
    nombre: "",
    contrasena: "",
    valid: true,
    credenciales_usuario: [],
 
  }),

  /* LOS MÉTODOS SIEMPRE FUERA DE DATA*/
  methods: {
    /* EL JSON ENVIADO DEBE TENER LOS MISMOS NOMBRES DEL*/
    async acceder(){
      axios.post('http://127.0.0.1:5000/login',{
        nickname: this.nombre,
        contraseña:this.contrasena
      },
      this.config_request)
      .then((res)=>{console.log(res.data);
      if(res.data.rol=== 1){
        console.log('al fin');
        this.$router.push("/admin");
      }
      else if(res.data.rol=== 2){
        this.$router.push("/");
      }
      else{
        this.$router.push("/logins")
      }
      })
      .catch((error)=>{console.log(error);})
    },
    registrar(){
      console.log('registrar');
      this.$router.push("/registro_user");
    },
    olvidar(){
      console.log('olvidar');
      this.$router.push("/forgot_pass");
    }
  },
};
</script>
<style>
.fondo3 {
  width: 100%;
  background: url("https://media.istockphoto.com/vectors/books-sketch-seamless-vector-id594484448?k=20&m=594484448&s=612x612&w=0&h=6lvNgspQuiOQUidxaH7LPfiE7RcicUgwReKe-WEhSNc=");
}
</style>
