<template>
    <ion-page>
        <ion-header>
        <ion-toolbar>
            <ion-title>Main Page</ion-title>
        </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true">
        <ion-header collapse="condense">
            <ion-toolbar>
            <ion-title size="large">Tab 1</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-grid>
            <ion-row class="ion-align-items-center">
            <ion-col size="4"></ion-col>
            <ion-col size="4" class="ion-text-center">
                <ion-item>
                    <ion-label>Enter ID here:</ion-label>
                    <ion-input id="id-field" aria-label="Enter ID here:"></ion-input>
                </ion-item>
                <ion-button color="primary" @click="getDistance()">Get data</ion-button>
                <lottie-player v-if="showImage" :src="imageSource" background="transparent" speed="1" style="width: 75%; height: 75%;" autoplay></lottie-player>
                <img v-if="showCapy" :src="imageSource" alt="">
            </ion-col>
            <ion-col size="4"></ion-col>
            </ion-row>
        </ion-grid>
        </ion-content>
    </ion-page>
</template>

<script>
import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonButton,
    IonGrid,
    IonCol,
    IonRow,
    IonInput
} from "@ionic/vue";
import { person } from 'ionicons/icons';

export default {
    name: "tab-page-1",
    data() {
        return {
            id: 0,
            personData: [],
            imageSource: "",
            showImage: false,
            showCapy: false
        }
    },
    components: {
        IonPage,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonButton,
        IonGrid,
        IonCol,
        IonRow,
        IonInput
    },
    methods: {
        receiveID() {
            this.id = document.getElementById("id-field").value;
            if(this.id != null) {
                return this.id;
            }
        },
        getDistance() {
            const personID = this.receiveID();
            const personData = [];
            let obj;
            this.showImage = false;

            fetch('https://api.thingspeak.com/channels/2094803/feeds.json?api_key=X6OZE8XX2HH3L7VF&results=8000')
                .then(res => res.json())
                .then(data => {
                    obj = data['feeds'];
                })
                .then(() => {
                    obj.forEach(element => {
                        try {
                            const newInt = parseInt(element[`field${personID}`])
                            if(!isNaN(newInt)) {
                                personData.push(newInt);
                            }
                        } catch (error) {
                            console.log(error)
                        }
                    });
                })
                .then(() => {
                    const sum = personData.reduce((partialSum, a) => partialSum + a, 0);
                    const avg = (sum / personData.length)

                    if(avg > 1) {
                        const rndInt = Math.floor(Math.random() * 1000);
                        if(rndInt == 69){
                            this.showCapy = true;
                            this.imageSource = "https://external-preview.redd.it/lPGMRn-cDmoLcOWEKqJIhiZKb35_nsdhBQLVon-8bo0.png?format=pjpg&auto=webp&s=827495651278171413c9c5e3fa5ec2411b0c8456"
                        } else if(rndInt == 420){
                            this.showCapy = true;
                            this.imageSource = "https://media.tenor.com/qu3ChHRA6O4AAAAd/gort.gif"
                        } else {
                            this.showImage = true
                            this.imageSource = "https://assets1.lottiefiles.com/packages/lf20_niyfyoqs.json"
                        }
                    } else {
                        this.showImage = true
                        this.imageSource = "https://assets5.lottiefiles.com/packages/lf20_pqpmxbxp.json"
                    }
                })
                .catch(error => console.error(error))
        }
    }
};
</script>
