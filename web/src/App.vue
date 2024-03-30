<template>
  <div>
    <div class="buttons">
      <el-button type="primary" @click="ShowPart1">Part One</el-button>
      <el-button type="primary" @click="ShowPart2">Part Two</el-button>
      <el-button type="primary" @click="ShowPart3">Part Three</el-button>
    </div>
    <div class="main">
      <MainContent></MainContent>
    </div>
    <div class="below">
      <InfoBelow></InfoBelow>
    </div>
  </div>
</template>

<script>
import MainContent from './components/MainContent.vue';
import InfoBelow from './components/InfoBelow.vue';
export default {
  name: 'App',
  components: {
    MainContent,
    InfoBelow,
  },
  methods:{
    ShowPart1(){
      this.$router.push({name:'PartOne'})
    },
    ShowPart2(){
      this.$router.push({name:'PartTwo'})
    },
    ShowPart3(){
      this.$router.push({name:'PartThree'})
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.buttons{
  display: flex;
  justify-content: center;
}
.main{
  margin-bottom: 200px;
}
.below{
  margin-top: 200px;
}
</style>
