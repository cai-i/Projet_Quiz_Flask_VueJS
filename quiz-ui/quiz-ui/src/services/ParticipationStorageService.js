

export default {
  clear() {
    // todo : implement
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    // todo : implement
    window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    // todo : implement
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    // todo : implement
    window.localStorage.getItem("participationScore");
  }
};