

export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem("participationScore");
  },
  saveAuthentificationToken(authentificationToken) {
    window.localStorage.setItem("authentificationToken", authentificationToken);
  },
  getAuthentificationToken() {
    return window.localStorage.getItem("authentificationToken");
  },
  removeAuthentificationToken() {
    return window.localStorage.removeItem("authentificationToken");
  },
};