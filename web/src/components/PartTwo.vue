<template>
    <div>
      <h2>part two</h2>
      <div class="content">
        <div>
            <el-button type="default" @click="RunCode">click me to run the code in part two</el-button>
        </div>
        <div class="items-container">
            <div v-for="(item, index) in items" :key="index" class="outer">
                <div class="inner">
                <h4>{{ item.name }}</h4>
                <h4>{{ item.actual }}</h4>
                <h4>{{ item.predicted }}</h4>
                </div>
            </div>
        </div>
        <div class="outer">
            <h4>Accuracy:</h4>
            <h4>{{ accuracy }}</h4>
        </div>
        </div>
    </div>
  </template>
  
  <script>
  import common from '../common/common';
  import axios from 'axios';
  import { ElMessage } from 'element-plus'
  
  export default {
    name: 'PartOne',
    data() {
      return {
        items: [],
        accuracy: '',
      }
    },
    methods: {
      async RunCode() {
        try {
          ElMessage("please wait...")
          await axios.post(common.backend_prefix + '/parttwo')
            .then(res => {
              if (res.data.status == 'fail') {
                ElMessage.error('There is an error occurred when running the part two code');
              } else {
                this.items = res.data.items;
                this.accuracy = res.data.accuracy;
              }
            })
            .catch(err => {
              ElMessage.error(err);
            })
        } catch {
          error => {
            ElMessage.error(error);
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
  
  .inner {
    display: flex;
    flex-direction: row;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width: 100%;
  }
  
  .inner:hover {
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
  