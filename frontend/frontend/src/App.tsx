import { Header } from './components/Header';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#ffffff'
    },
    secondary: {
      main: '#ebe9e9'
    }
  }
});

const App = () => {
  
  return (
    <ThemeProvider theme={theme}>
      <Header />
    </ThemeProvider>
  );
};



export default App;
