import axios from 'axios';

const defaultValidateStatus = (status) => {
  return status < 400;
}

class ApiUtil {
  constructor() {
    this._history = null;
  }

  get history() {
    return this._history;
  }

  set history (history) {
    this._history = history;
  }

  axiosInstance(validateStatusFunc = defaultValidateStatus) {
    const instance = axios.create({
      headers: {
        'Accept': 'application/json'
      },
      validateStatus: validateStatusFunc
    });
    instance.interceptors.response.use(null, error => {
      return Promise.reject(error);
    });
    return instance;
  }
}

const apiUtil = new ApiUtil();
export default apiUtil;