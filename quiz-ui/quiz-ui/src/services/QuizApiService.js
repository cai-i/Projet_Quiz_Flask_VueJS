import axios from "axios";
import ParticipationStorageService from "./ParticipationStorageService";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

import participationStorageService from "./ParticipationStorageService";

export default {
  async call(method, resource, data = null, token = participationStorageService.getAuthentificationToken()) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", "questions?position=" + position);
  },
  getToken(pw) {
    return this.call("post", "login", {"password": pw});
  },
  submitAnswers(playerName, answers) {
    return this.call("post", "participations", { "playerName": playerName, "answers": answers });
  },
  putQuestion(question) {
    return this.call("put", "questions/" + question.id, {
      "text": question.questionText,
      "title": question.questionTitle,
      "image": question.questionImage,
      "position": question.position,
      "possibleAnswers": question.possibleAnswers
  });
  },
};