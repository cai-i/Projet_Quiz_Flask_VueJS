<template>
    <div class="outerCircle"></div>
    <div class="innerCircle"></div>
    <div class="icon"></div>
</template>

<style scoped>
/* Loading animation */
.outerCircle {
  background-color: transparent;
  border: 8px solid rgba(97, 82, 72, 0.9);
  opacity: 0.9;
  border-right: 5px solid transparent;
  border-left: 5px solid transparent;
  border-radius: 100px;
  width: 103px;
  height: 103px;
  margin: 0 auto;
  -moz-animation: spinPulse 3s infinite ease-in-out;
  -webkit-animation: spinPulse 3s infinite ease-in-out;
}
.innerCircle {
  background-color: transparent;
  border: 5px solid rgba(189, 215, 60, 0.6);
  opacity: 0.9;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-radius: 100px;
  top: -100px;
  width: 92px;
  height: 92px;
  margin: 0 auto;
  position: relative;
  -moz-animation: spinoffPulse 1s infinite linear;
  -webkit-animation: spinoffPulse 1s infinite linear;
}

@-moz-keyframes spinPulse {
  0% {
    -moz-transform: rotate(160deg);
    opacity: 0;
    box-shadow: 0 0 1px #bdd73c;
  }
  50% {
    -moz-transform: rotate(145deg);
    opacity: 1;
  }
  100% {
    -moz-transform: rotate(-320deg);
    opacity: 0;
  }
}
@-moz-keyframes spinoffPulse {
  0% {
    -moz-transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(360deg);
  }
}
@-webkit-keyframes spinPulse {
  0% {
    -webkit-transform: rotate(160deg);
    opacity: 0;
    box-shadow: 0 0 1px #bdd73c;
  }
  50% {
    -webkit-transform: rotate(145deg);
    opacity: 1;
  }
  100% {
    -webkit-transform: rotate(-320deg);
    opacity: 0;
  }
}
@-webkit-keyframes spinoffPulse {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
</style>



<script>
export default {
    name: "LoadAnim"
} 
</script>