import apiUtil from './ApiUtil';

export {
  getLeaderboards,
  getSubsiteLocations,
  getGenera,
  getGenusDistribution
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

const getGenera = () => {
  const url = apiRoot + '/api/v0/genera';
  return apiUtil.axiosInstance().get(url);
}

const getGenusDistribution = (genus) => {
  const url = apiRoot + '/api/v0/genera/' + genus;
  return apiUtil.axiosInstance().get(url);
}