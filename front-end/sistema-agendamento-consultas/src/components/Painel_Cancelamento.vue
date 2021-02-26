<template>
<div>
    <div class='defocus' @click="handleClick(false)">
    </div>
    <div  class="card" 
        style="width: 30rem; top: 30%; left: 37.5%; z-index: 9999; position: fixed;">
            <span class="card-header text-light bg-dark">
            <h5 style="text-align: center;">
                AVISO
                <button @click="handleClick(false)" type="button" class="close" data-dismiss="card" aria-label="Close">
                    <span aria-hidden="true" class="text-white" style="font-size: 35px;">&times;</span>
                </button>
            </h5>
            </span>
            <span style = "text-align: justify; margin-left: 5%; margin-right: 5%; text-align: center;">
                <br>
                    {{message}} 
                <br>
                <br>
            </span>
    </div>
</div>
</template>

<script>
import moment from 'moment'
export default {
    props: {
        date: {
            type: Number,
            require: false
        }
    },
    created() {
        this.computeDeadline()
    },
    data() {
        return {
            currentDate: moment().format('YYYY-MM-DD'),
            deadline: '',
            message: ''
        }
    },
    methods: {
        handleClick(arg) {
            this.$emit('showPanel', arg)
        },
        confirmCancellation() {
            this.$emit('confirmedCancellation', true)
        },
        computeDeadline() {
            this.deadline = moment(this.date).subtract(3,'d').format('YYYY-MM-DD')
            if (moment(this.currentDate).isBefore(this.deadline, 'day')) {
                this.message = "O paciente tem até o dia " + moment(this.deadline).format('DD/MM/YYYY') + ' para cancelar a consulta. Caso contrário, pagará multa.'
            } else if (moment(this.deadline).isBefore(this.currentDate, 'day')) {
                this.message = "O prazo de cancelamento para essa consulta finalizou. O cancelamento na data atual implicará na cobraça de uma multa."
            }
        }
    }
}
</script>

<style scoped>
.defocus {
  position: fixed;
  z-index: 2;
  top: 0;
  left: 0;
  width: 200%;
  height: 100%;
  background-color: rgba(162, 162, 162, 1);
  display: table;
  opacity: 0.75;
  transition: opacity .3s ease;
}
</style>>