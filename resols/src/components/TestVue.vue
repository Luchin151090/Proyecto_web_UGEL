<template>
<v-card fluid class="ma-5">
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="filteredDesserts"
      show-select
      item-key="name"
    >
    <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="downloadItem(item)">
          mdi-download
          
        </v-icon>
       
      </template>
      <template v-slot:header="{ }">
        
        <tr class="grey lighten-3">
          <th>
            <v-icon>mdi-filter</v-icon>
          </th>
          <th v-for="header in headers" :key="header.text">
            <div v-if="filters.hasOwnProperty(header.value)">
              <v-autocomplete
                flat
                hide-details
                multiple
                attach
                chips
                dense
                clearable
                :items="columnValueList(header.value)"
                v-model="filters[header.value]"
              >
                <template v-slot:selection="{ item, index }">
                  <v-chip v-if="index < 5">
                    <span>
                      {{ item }}
                    </span>
                  </v-chip>
                  <span v-if="index === 5" class="grey--text caption">
                    (+{{ filters[header.value].length - 5 }} others)
                  </span>
                </template>
              </v-autocomplete>
            </div>
          </th>
        </tr>
      </template>
    </v-data-table>
    <v-tour name="myTour" :steps="steps"></v-tour>
  
</v-card>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      selected: [],
      headers: [
        {
          text: "N° ID",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "N° Proyecto", value: "nproyecto" },
        { text: "Concepto", value: "concepto" },
        { text: "Descripción", value: "descripcion" },
        { text: "Monto", value: "monto" },
        { text: "Distrito", value: "distrito" },
        { text: "F.Emision", value: "Femision" },
        { text: "F.Noti", value: "Fnotificacion" },
        { text: "Actions",value:"actions",sortable:false}
      ],
      steps:[
        {
            target :'.v-step-0',
            content:'Hola Usuario aquí podrás <strong>buscar tu documento</strong>'
          },
          {
            target :'#v-step-1',
            content:'Usa el botón de descargar para obtener el documento<strong>buscar tu documento</strong>'
          },
      ],
      items: [],
      filters: {
        nproyecto: [],
        concepto: [],
        descripcion: [],
        monto: [],
        distrito: [],
        Femision: [],
        Fnotificacion:[],
      },
      
      
    };
  },
  mounted(){
    this.$tours['myTour'].start()
  },
  computed: {
    filteredDesserts() {
      return this.items.filter((d) => {
        return Object.keys(this.filters).every((f) => {
          return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
        });
      });
    },
  },
  async created(){
    axios
      .get("http://127.0.0.1:5000/resolucion/", this.config_request)
      .then((res) => {
        this.items = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    columnValueList(val) {
      return this.items.map((d) => d[val]);
    },
    async downloadItem(item){
      console.log("item :", item.id);
     axios
      .get("http://127.0.0.1:5000/download_file/"+item.id.toString(),{
        responseType:"blob",
      })
      .then((res)=>{
          let blob = new Blob([res.data],{type:'application/pdf'});
          let link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);
          console.log(res.data);
          link.download = item.nproyecto+item.concepto;
          link.click();

      })
      .catch((error)=>{
        console.log(error);
      })
  
    },
  },
  
};
</script>
<style>
</style>
