<template>
<div class="col d-flex justify-content-center">
    <div class="card" style="width: 70%;"> 
        <div class='card-header' style="background-color: #43A390;">
            <h3>Política de Agendamento</h3>
        </div>
        <br>
        <h5><b>Turno de Atendimento:</b></h5>
        <p>Turno de atendimento para pacientes <b> pertencentes ao grupo de risco</b>:
            <select v-model="selectedOption">
                <option>Manhã</option>
                <option>Tarde</option>
            </select>
        </p>
        <p class="note"> 
            Para dar prioridade ao atendimento de pessoas pertencentes ao grupo de risco e aplicar medidas de segurança mais
            estritas para os pacientes desse grupo, a clínica pode definir um período onde somente essas pessoas serão atendidas
            e um protocolo mais rigoroso será seguido. 
        </p>
        <p>Turno de atendimento para pacientes <b> não pertencentes ao grupo de risco</b>:
            <span v-if="selectedOption == 'Tarde'">Manhã</span>
            <span v-if="selectedOption == 'Manhã'">Tarde</span>
        </p>
        <hr>
        <h5><b>Capacidade de Pessoas: </b></h5>
        <p><b>Capacidade</b> de pessoas na clínica no <b> turno regular: </b><input v-model="regularCapacity" type="number" min="0"></p>
        <p class="note"> 
            É importante limitar a quantidade de pacientes na clínica para evitar aglomerações. Deve-se levar em consideração o distanciamento
            mínimo entre os indivíduos para evitar a transmissão do vírus.
        </p><br>
        <p><b>Capacidade</b> de pessoas na clínica no <b> turno de atendimento ao grupo de risco: </b><input v-model="riskGroupCapacity" type="number" min="0"></p>
         <p class="note"> 
            Uma vez que pacientes do grupo de risco tendem a ser mais vulneráveis à COVID-19, é importante que as medidas de segurança 
            sejam ainda mais estritas, então sugere-se restringir ainda mais a quantidade de pessoas permitidas na clínica.
        </p>
        <hr>
        <h5><b>Outras regras de segurança:</b></h5>
        <label><b>No turno regular: </b></label>
        <textarea
            v-model = "regularProtocols"
            placeholder = "Inserir a descrição textual dos protocolos seguidos pela clínica no turno regular. Por exemplo: a clínica disponibiliza álcool em gel gratuitamente para os pacientes; todos os indivíduos na clínica são obrigados a usar máscara; etc."
        >     
        </textarea>
        <label><b>No turno de atendimento ao grupo de risco: </b></label>
        <textarea
            v-model = "riskGroupProtocols"
            placeholder = "Inserir a descrição textual dos protocolos seguidos pela clínica no turno de atendimento ao grupo de risco. Além das regras especificadas para o turno regular, quais outros cuidados precisam ser tomados?"
        >     
        </textarea>
        <br>
        <button class="btn btn-success" @click="createSchedulingPolicy()">Salvar Alterações</button>
        <br><br>
    </div>      
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readSchedulingPolicy()
    },
    watch: {
        selectedOption: function(newValue, oldValue) {
            if (newValue == 'Manhã'){
                this.regularGroupInterval = 'Tarde'
                this.riskGroupInterval = 'Manhã' 
            } else {
                this.regularGroupInterval = 'Manhã'
                this.riskGroupInterval = 'Tarde'
            }
        }
    },
    data () {
        return {
            selectedOption: '',
            regularGroupInterval: '',
            riskGroupInterval: '',
            regularCapacity: '',
            riskGroupCapacity: '', 
            regularProtocols: '',
            riskGroupProtocols: ''
        }
    },
    methods: {
        readSchedulingPolicy() {
            httpRequests.readAll('politica_agendamento').then(response => {
                this.selectedOption = response.data.objects[0].PltAgd_Turno_Grupo_Risco
                this.regularGroupInterval = response.data.objects[0].PltAgd_Turno_Regular
                this.riskGroupInterval = response.data.objects[0].PltAgd_Turno_Grupo_Risco
                this.regularCapacity = response.data.objects[0].PltAgd_Capacidade_Regular
                this.riskGroupCapacity = response.data.objects[0].PltAgd_Capacidade_Grupo_Risco
                this.regularProtocols = response.data.objects[0].PltAgd_Protocolos_Regular
                this.riskGroupProtocols = response.data.objects[0].PltAgd_Protocolos_Grupo_Risco
            })
        },
        createSchedulingPolicy () {
            httpRequests.create('politica_agendamento', 
                {   'PltAgd_Turno_Regular': this.regularGroupInterval,
                    'PltAgd_Turno_Grupo_Risco': this.riskGroupInterval,
                    'PltAgd_Capacidade_Regular': this.regularCapacity,
                    'PltAgd_Capacidade_Grupo_Risco': this.riskGroupCapacity,
                    'PltAgd_Protocolos_Regular': this.regularProtocols,
                    'PltAgd_Protocolos_Grupo_Risco': this.riskGroupProtocols,

                }
            ).then(() => { 
            })
        }
    }
    
}
</script>

<style>
body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
  background-color: #D5E6E6;
}
h3 {
    text-align: center;
    color: white;
}
textarea {
    margin-left: 10%;
    margin-right: 10%;
    height: 7.5em;
    margin-bottom: 1%;
}
p, label {
    margin-left: 10%;
    margin-right: 10%;
}
.note {
    font-size: 0.9em; 
    color: red;
}
h5 {
    margin-left: 10%;
}
button {
    margin-left: 42.5%;
    margin-right: 42.5%;
}

</style>