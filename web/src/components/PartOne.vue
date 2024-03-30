<template>
  <div>
    <h2>part one</h2>
    <div class="content">
    <div>
        <el-button type="default" @click="RunCode">click me to run the code in part one</el-button>
    </div>
    <div class="items-container">
        <div v-for="item in items " :key="item" class="outer">
            <h2 v-if="item.flag == '1'">Datasets with feature selection:</h2>
            <h2 v-if="item.flag == '2'">Datasets without feature selection:</h2>
            <div class="inner">
                <h3>{{ item.name }}</h3>
                <h3>  :  </h3>
                <h3>{{ item.value }}</h3>
            </div>
            <el-divider v-if="item.name == 'knn'"></el-divider>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
import common from '../common/common';
import axios from 'axios';
import {ElMessage} from 'element-plus'
export default {
    name:'PartOne',
    data(){
        return{
            items:[],
        }
    },
    methods:{
        async RunCode(){
            try{
                ElMessage("please wait...");
                await axios.post(common.backend_prefix+'/partone')
                .then(
                    res =>{
                        if(res.data.status == 'fail'){
                            ElMessage.error(res.data.message)
                        }else{
                            this.items = res.data;
                        }
                    }
                ).catch(
                    err =>{
                        ElMessage.error(err)
                    }
                )
                }catch{
                    error =>{
                        ElMessage.error(error)
                    }
                }
            }
        }
}
</script>

<style>
.outer {
    display: flex;
    justify-content: center;
    flex-direction: column;
}
.inner{
    display: flex;
    flex-direction: row;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width:30%;
}
.inner:hover{
    background-color: floralwhite;
}
.content {
  display: flex;
  flex-direction: column;
  align-items: center; /* 沿着主轴居中对齐 */
}

.items-container {
  margin-top: 20px; /* 设置顶部间距 */
}

</style>