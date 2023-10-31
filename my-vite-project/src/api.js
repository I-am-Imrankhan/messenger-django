import axios from "axios";

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL || "",
    headers: {
        "Content-type": "application/json",
    },
    withCredentials: true,
    xsrfHeaderName: "X-CSRFToken",
    xsrfCookieName: "csrftoken",
});

export default apiClient;
