<template>
  <v-container>
    <v-card fluid
    height="500"
    width="97%"
    class="ma-6"
    >
    <v-img
    max-height="50"
    src="https://png.pngtree.com/thumb_back/fw800/background/20190222/ourmid/pngtree-autumn-rice-field-scarecrow-background-material-seasonfallautumn-backgroundbeautiful-backgroundfallen-image_53557.jpg"></v-img>
      <v-card-title>Actualizar información</v-card-title>
        <v-form class="ma-10">
            <v-text-field label="Nombre" placeholder="Nombre"></v-text-field>
            <v-text-field label="Apellidos" placeholder="Apellidos"></v-text-field>
            <v-text-field label="Nueva Contraseña" placeholder="Contraseña" type="password"></v-text-field>
            <v-text-field label="Repita Contraseña" placeholder="Confirmar Contraseña"></v-text-field>
            <v-btn>Guardar</v-btn>


        </v-form>
        
    </v-card>
    

        <v-row>
            <v-col cols="9">
                <v-card  height="300">

                </v-card>
            </v-col>
            <v-col cols="3">
                <v-card  height="300">

                </v-card>
            </v-col>

        </v-row>
    </v-container>

</template>