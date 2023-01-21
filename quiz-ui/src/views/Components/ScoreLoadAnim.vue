<template>
    <div class="skill">
        <div class="outer">
        <div class="inner">
            <div class="number">
            {{ this.scoreDisplay }}
            </div>
        </div>
        </div>
        <svg
        xmlns="http://www.w3.org/2000/svg"
        version="1.1"
        width="160px"
        height="160px"
        >
        <defs>
            <linearGradient id="GradientColor">
            <stop offset="0%" stop-color="#e91e63" />
            <stop offset="100%" stop-color="#673ab7" />
            </linearGradient>
        </defs>
        <circle
            cx="80"
            cy="80"
            r="70"
            stroke-linecap="round"
            :style="circleStyle"
        />
        </svg>
    </div>
</template>

<style scoped>

/* Animation pour le score rate  */
.skill {
  width: 160px;
  height: 160px;
  position: relative;
}

.outer {
  height: 160px;
  width: 160px;
  border-radius: 50%;
  padding: 20px;
  box-shadow: 6px 6px 10px -1px rgba(0, 0, 0, 0.25),
    -6px -6px 10px -1px rgba(255, 255, 255, 0.25);
}

.inner {
  height: 120px;
  width: 120px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 4px 4px 6px -1px rgba(0, 0, 0, 0.25),
    inset -4px -4px 6px -1px rgba(255, 255, 255, 0.25),
    -0.5px -0.5px 0px rgba(255, 255, 255, 0.5),
    0.5px 0.5px 0px rgba(0, 0, 0, 0.15), 0px 12px 10px rgba(0, 0, 0, 0.05);
}

.number {
  font-size: xxx-large;
  font-weight: bold;
  color: #555;
}

circle {
  fill: none;
  stroke: url(#GradientColor);
  stroke-width: 20px;
  stroke-dasharray: 472;
  stroke-dashoffset: 472;
  animation: anim 2s linear forwards;
}

svg {
  position: absolute;
  transform: rotate(-90deg);
  top: 0;
  left: 0;
}

@keyframes anim {
  100% {
    stroke-dashoffset: var(--sratio);
  }
}
</style>



<script>

export default {
  name: "ScoreLoadAnim",
  props: ['userScore','nbr_questions'],
 
  data() {
    return {
      scoreDisplay: "",
      circleStyle: {
        "--sratio": null,
        animationPlayState: "paused",
      }
    }
  },      
  async created() {    
      this.circleStyle["--sratio"] =
        472 * (1 + 0.05 - this.userScore / this.nbr_questions) - 1;
      if (this.userScore == 0) this.circleStyle["--sratio"] = 470;

      this.loadScore();
  },
  methods : { 
    loadScore : function() {        
      this.circleStyle.animationPlayState = "running";
      // Cas score de 0
      if (this.userScore == 0) {
        return (this.scoreDisplay = "0%");
      }
      // Cas score sup a 0
      var counter = 0;
      var incr = parseInt((10 * this.userScore) / this.nbr_questions, 10);
      setInterval(() => {
        if (counter >= (100 * this.userScore) / this.nbr_questions - 10) {
          incr = 1;
        }
        if (counter >= (100 * this.userScore) / this.nbr_questions -1) {
          clearInterval();
        } else {
          counter += incr;
          this.scoreDisplay = counter + "%";
        }
      });
    }
  }   
}
 
</script>