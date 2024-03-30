import {createRouter,createWebHistory} from 'vue-router';

import PartOne from '../components/PartOne.vue';
import PartTwo from '../components/PartTwo.vue';
import PartThree from '../components/PartThree.vue';

const routes = [
    {path:'/',redirect:'/PartOne'},
    { path :'/PartOne',name:'PartOne',components:{PartOne:PartOne}},
    { path : '/PartTwo',name:'PartTwo',components:{PartTwo:PartTwo}},
    { path : '/PartThree',name:'PartThree',components:{PartThree:PartThree}},
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router