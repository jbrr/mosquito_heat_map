import apiUtil from './ApiUtil';

export {
  getLeaderboards,
  getSubsiteLocations
};

const apiRoot = process.env.API_ROOT

const getSubsiteLocations = () => {
  const url = apiRoot + '/api/v0/locations';
  return apiUtil.axiosInstance().get(url);
}

const getLeaderboards = () => {
  const url = apiRoot + '/api/v0/leaderboards';
  return apiUtil.axiosInstance().get(url);
}