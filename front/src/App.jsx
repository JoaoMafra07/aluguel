import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './pages/login'
import HomeUser from './pages/user/home'
import PropertiesUser from './pages/user/properties'
import PaymentsUser from './pages/user/contracts'
import ContractsUser from './pages/user/payments'

import HomeAdmin from './pages/admin/home'
import PropertiesAdmin from './pages/admin/properties'
import PaymentsAdmin from './pages/admin/payments'
import ContractAdmin from './pages/admin/contracts'

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Login/>} />
        <Route path='/login/' element={<Login/>} />
        <Route path='/user/home/' element={<HomeUser/>}/>
        <Route path='/user/properties/' element={<PropertiesUser/>}/>
        <Route path='/user/contracts/' element={<ContractsUser/>}/>
        <Route path='/user/payments/' element={<PaymentsUser/>}/>
        <Route path='/admin/home/' element={<HomeAdmin/>}/>
        <Route path='/admin/properties/' element={<PropertiesAdmin/>}/>
        <Route path='/admin/contracts/' element={<ContractAdmin/>}/>
        <Route path='/admin/payments/' element={<PaymentsAdmin/>}/>
      </Routes>
    </Router>
  )
}
