<template>
  <div>
    <el-link type="primary" @click="showmembers = true">click me to see the group members</el-link>
    <el-dialog v-model="showmembers">
        <div class="team-members">
        <div class="member-card">
            <div class="member-name">Wang Guanchao</div>
            <div class="member-id">tjut id: 20212709</div>
        </div>
        <div class="member-card">
            <div class="member-name">Hu Xiaoyue</div>
            <div class="member-id">tjut id:20212721 </div>
        </div>
        <div class="member-card">
            <div class="member-name">Pan Xianghao</div>
            <div class="member-id">tjut id: 20212707</div>
        </div>
        <div class="member-card">
            <div class="member-name">Ge Chang</div>
            <div class="member-id">tjut id: 20212720</div>
        </div>
        <div class="member-card">
            <div class="member-name">Song Zhuoao</div>
            <div class="member-id">tjut id: 20212708</div>
        </div>
        </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
    name:'InfoBelow',
    data(){
        return{
            showmembers:false
        }
    }
}
</script>

<style>
  .team-members {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
  }
  .member-card {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    padding: 15px;
    width: calc(25% - 20px);
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  .member-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  }
  .member-name {
    font-size: 24px;
    color: #333;
    margin-bottom: 5px;
  }
  .member-id {
    font-size: 18px;
    color: #555;
  }
</style>