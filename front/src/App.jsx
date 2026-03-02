import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './pages/login'
import HomeUser from './pages/home_user'
import ImovelUser from './pages/imovel_user'
import ContratoUser from './pages/contrato_user'
import PagamentoUser from './pages/pagamento_user'

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Login/>} />
        <Route path='/login/' element={<Login/>} />
        <Route path='/homeuser/' element={<HomeUser/>}/>
        <Route path='/imoveluser/' element={<ImovelUser/>}/>
        <Route path='/contratouser/' element={<ContratoUser/>}/>
        <Route path='/pagamentouser/' element={<PagamentoUser/>}/>
      </Routes>
    </Router>
  )
}
