import React from 'react'
import { getLeaderboards } from '../../utils/Apis';

class LeaderboardContainer extends React.Component {
  constructor(props) {
    super(props);
    this.displayEachRow = this.displayEachRow.bind(this);
    this.state = {
      leadersByPerson: [],
      leadersByLab: [],
      isLoaded: false
    };
  }

  componentDidMount() {
    getLeaderboards()
    .then(result => {
      this.setState({
        leadersByPerson: result.data.byScientist,
        leadersByLab: result.data.byLaboratory,
        isLoaded: true
      });
    })
    .catch(error => {
      this.setState({
        isLoaded: true,
        error
      })
    })
  }

  displayEachRow(data) {
    var listElements = data.map((item) => {
      return <li>{item[0]}: {item[1]}</li>
    });

    return listElements;
  }

  render() {
    const isLoaded = this.state.isLoaded;
    const error = this.state.error;
    const leadersByPerson = this.state.leadersByPerson;
    const leadersByLab = this.state.leadersByLab;
    const leadersByPersonList = this.displayEachRow(leadersByPerson);
    const leadersByLabList = this.displayEachRow(leadersByLab);
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return(
        <div className='col-9 leaderboard-container' id='leaderboard'>
          <h1>By Person</h1>
          <ol>
            {leadersByPersonList}
          </ol>
          <h1>By Lab</h1>
          <ol>
            {leadersByLabList}
          </ol>
        </div>
      )
    }
  }
}

export default LeaderboardContainer;