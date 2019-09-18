import React from 'react'
import { Transition, TransitionGroup } from 'react-transition-group';
import { getLeaderboards } from '../../utils/Apis';
import Loader from '../../components/Loader';

class LeaderboardContainer extends React.Component {
  constructor(props) {
    super(props);
    this.displayEachRow = this.displayEachRow.bind(this);
    this.displayLeaderboard = this.displayLeaderboard.bind(this);
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
      // API returns ID, name, and count of mosquitos identified
      // Cause React keeps harassing me about having a unique idenfier for each list element 🙄
      return <li key={ item[0] }>{ item[1] }: { item[2] }</li>
    });

    return listElements;
  }

  displayLeaderboard() {
    const leadersByPerson = this.state.leadersByPerson;
    const leadersByLab = this.state.leadersByLab;
    const leadersByPersonList = this.displayEachRow(leadersByPerson);
    const leadersByLabList = this.displayEachRow(leadersByLab);
    if (this.state.error) {
      return <div>Error: {this.state.error.message}</div>;
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
      );
    }
  }

  render() {
    const isLoaded = this.state.isLoaded;
    const display = this.state.isLoaded ? ['leaderboard', this.displayLeaderboard()] : ['loader', <Loader />];
    return (
      <TransitionGroup className='this-ol-map'>
        <Transition key={ display[0] } in={ isLoaded } timeout={ 350 }>
          { display[1] }
        </Transition>
      </TransitionGroup>
    );  }
}

export default LeaderboardContainer;