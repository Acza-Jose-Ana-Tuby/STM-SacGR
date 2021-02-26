<template>
<div>
    <div class='defocus' @click="handleClick(false)">
    </div>
    <div  class="card" 
        style="width: 30rem; top: 30%; left: 37.5%; z-index: 9999; position: fixed;">
            <span class="card-header text-light bg-dark">
            <h5 style="text-align: center;">
                Info
                <button @click="handleClick(false)" type="button" class="close" data-dismiss="card" aria-label="Close">
                    <span aria-hidden="true" class="text-white" style="font-size: 35px;">&times;</span>
                </button>
            </h5>
            </span>
            <span style = "text-align: justify; margin-left: 5%; margin-right: 5%">
                <br>
                A OMS considera como grupo de risco: bebês e crianças menores de seis anos, 
                gestantes, mulheres que deram a luz há menos de quarenta dias, maiores de sessenta anos 
                e pessoas portadoras de comorbidades, como diabetes, hipertensão arterial, doenças do coração, 
                pulmão e rins, portadores de imunossupressão e pacientes em tratamento contra o câncer.
                <br>
                <br>
            </span>
    </div>
</div>
</template>

<script>
export default {
    methods: {
        handleClick(arg) {
            this.$emit('showPanel', arg)
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
  width: 100%;
  height: 100%;
  background-color: rgba(162, 162, 162, 1);
  display: table;
  opacity: 0.75;
  transition: opacity .3s ease;
}
</style>>