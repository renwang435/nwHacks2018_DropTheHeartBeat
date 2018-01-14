import React, {Component} from 'react';
import PropTypes from 'prop-types';
/*import ListItem from './ListItem';*/
import logo from './logo.svg';
import './App.css';
import {List, ListItem} from 'material-ui/List';
import IconButton from 'material-ui/IconButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import ActionDone from 'material-ui/svg-icons/action/done';


class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            entries: [{
                id: 1,
                text: 'clean room'
            }, {
                id: 2,
                text: 'wash the dishes'
            }, {
                id: 3,
                text: 'feed my cat'
            }]
        };

        this.removeElement = this.removeElement.bind(this);
    }

    static childContextTypes =
        {
            muiTheme: PropTypes.object
        };

    getChildContext()
    {
        return {
            muiTheme: getMuiTheme()
        }
    }

    iconButtonElement = (
        <IconButton touch={true}>
        </IconButton>
    );

    removeElement(key) {
        const remainder = this.state.entries.remove(key);
        this.setState({entries: remainder});
    }

    renderListItem(val, key) {
        return <ListItem key={key} primaryText={val.text} rightIconButton={<ActionDone value={key} onClick={() => this.removeElement(key)}/>}/>
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">Welcome</h1>
                </header>
                <p className="Queue-Title">
                    Patient Queue:
                </p>
                <div>
                    <List>
                        {this.state.entries.map(this.renderListItem)}
                    </List>
                </div>
                <p className="HeatMap-Title">
                    Heat Map:
                </p>
            </div>
        )
    }
}


/*  renderListItem(val, key) {
    return <ListItem key={key} value={val} />
  }

  render() {
    const stringList = [[1,3,4,5], [1,2,3,4], [1,2,3,4]];

    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome</h1>
      </header>
        <p className="Queue-Title">
          Patient Queue:
        </p>
        {stringList.map(this.renderListItem)}
      </div>

    );
  }
} */

export default App;
