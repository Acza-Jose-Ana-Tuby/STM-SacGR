<template>
    <FullCalendar 
        :options="calendarOptions" 
        style="margin: auto; width: 90%;"
    />
</template>

<script>
import moment from 'moment'
import httpRequests from '../http-requests'
import FullCalendar from '@fullcalendar/vue'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
export default {
    created() {
        this.readSchedulingPolicy()
        this.readDoctorSchedules()
    },
    components: {
        FullCalendar 
    },
    props: {
        riskGroupBelonging: {
            type: Number,
            require: false
        },
        doctorID: {
            type: Number,
            require: false
        }
    },
    data() {
        return {
            schedules: [],
            lastClickedEvent: '',
            schedulingPolicies: [],
            calendarOptions: {
                plugins: [ interactionPlugin, timeGridPlugin ],
                initialView: 'timeGridWeek',
                locale: 'pt-br',
                allDaySlot: false,
                buttonText: {today: 'Retonar à data atual'},
                displayEventTime: false,
                events: [],
                slotMinTime: '07:00:00',
                slotMaxTime: '19:00:00',
                slotLabelInterval: '00:05',
                stickyFooterScrollbar: false,
                handleWindowResize: false,
                contentHeight: 'auto',
                eventClick: (info) => {
                    if (this.lastClickedEvent) this.lastClickedEvent.setProp('backgroundColor', 'blue')
                    let event = info.event
                    event.setProp('backgroundColor', 'green')
                    this.lastClickedEvent = event
                    this.$emit('doctorScheduleID', event.id)
                }
            },
        }
    },
    methods: {
        readSchedulingPolicy() {
            httpRequests.readAll('politica_agendamento')
                .then(response => {
                    this.schedulingPolicies = response.data.objects[0]
                    this.computeLimitTimes()
                })
        },
        readDoctorSchedules() {
            this.calendarOptions.events = []
            httpRequests.readAll('agenda_medica')
                .then(response => {
                    for (let schedule of response.data.objects) {
                        if (schedule.AgdMed_Med_ID == this.doctorID) {
                            let start = schedule.AgdMed_Dia + 'T' + schedule.AgdMed_Hora_Inicio
                            let end = moment(schedule.AgdMed_Dia + 'T' + schedule.AgdMed_Hora_Inicio).add(moment.duration(parseInt(schedule.AgdMed_Duracao), 'minutes')).format('YYYY-MM-DDTHH:mm')
                            this.calendarOptions.events.push(
                                {
                                    id: schedule.AgdMed_ID,
                                    title: start.slice(11, 16) + '-' + end.slice(11, 16),
                                    start: start,
                                    end: end,
                                    backgroundColor: 'blue'
                                }
                            )
                        }
                    }
                })
        },
        computeLimitTimes() {
            if (this.$route.name == "AgendaMedica") {
                this.calendarOptions.slotMinTime = '06:00:00'
                this.calendarOptions.slotMaxTime = '18:00:00'
            } else if (this.schedulingPolicies.PltAgd_Turno_Grupo_Risco == 'Manhã' && this.riskGroupBelonging == 1) {
                this.calendarOptions.slotMinTime = '06:00:00'
                this.calendarOptions.slotMaxTime = '12:00:00'
            } else if (this.schedulingPolicies.PltAgd_Turno_Grupo_Risco == 'Tarde' && this.riskGroupBelonging == 1) {
                this.calendarOptions.slotMinTime = '12:00:00'
                this.calendarOptions.slotMaxTime = '18:00:00'
            } else if (this.schedulingPolicies.PltAgd_Turno_Grupo_Risco == 'Manhã' && this.riskGroupBelonging == 0) {
                this.calendarOptions.slotMinTime = '12:00:00'
                this.calendarOptions.slotMaxTime = '18:00:00'
            } else if (this.schedulingPolicies.PltAgd_Turno_Grupo_Risco == 'Tarde' && this.riskGroupBelonging == 0) {
                this.calendarOptions.slotMinTime = '06:00:00'
                this.calendarOptions.slotMaxTime = '12:00:00'
            }

        }
    }
}
</script>

<style scoped>
</style>