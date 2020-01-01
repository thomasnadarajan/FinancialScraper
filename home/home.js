/*
const React = require('react');
const ReactDOM = require('react-dom'); 
const Paper = require('@material-ui/core/Paper')
const Grid = require('@material-ui/core/Grid')
const {makeStyles} = require('@material-ui/core/styles')
*/
const React = require('react');
const ReactDOM = require('react-dom');
const { makeStyles } = require('@material-ui/core/styles');
const Paper = require('@material-ui/core/Paper');
const Grid = require('@material-ui/core/Grid');
const useStyles = makeStyles(theme => ({
    root: {
      flexGrow: 1,
    },
    paper: {
      padding: theme.spacing(2),
      textAlign: 'center',
      color: theme.palette.text.secondary,
    },
  }));
class HomeScreen extends React.Component {
    render() {
        const classes = useStyles();
        return (
            <div className={classes.root}>
              <Grid container spacing={3}>
                <Grid item xs={12}>
                  <Paper className={classes.paper}>xs=12</Paper>
                </Grid>
                <Grid item xs={6}>
                  <Paper className={classes.paper}>xs=6</Paper>
                </Grid>
                <Grid item xs={6}>
                  <Paper className={classes.paper}>xs=6</Paper>
                </Grid>
                <Grid item xs={3}>
                  <Paper className={classes.paper}>xs=3</Paper>
                </Grid>
                <Grid item xs={3}>
                  <Paper className={classes.paper}>xs=3</Paper>
                </Grid>
                <Grid item xs={3}>
                  <Paper className={classes.paper}>xs=3</Paper>
                </Grid>
                <Grid item xs={3}>
                  <Paper className={classes.paper}>xs=3</Paper>
                </Grid>
              </Grid>
            </div>
          );
    }
}

ReactDOM.render(<HomeScreen />, document.querySelector("#root"));