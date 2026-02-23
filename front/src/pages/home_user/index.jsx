import React, {useEffect} from "react"
import axios from 'axios'

export default function HomeUser(){

    // const token = localStorage.getItem('token')

    const listar = async ()=>{
        const response = await axios.get('http://127.0.0.1:8000/api/usuarios')
        console.log("Lista de usuários: ", response.data);
    }

    useEffect(()=>{listar()}, []) // useEffect serve para carregar os itens assim que a página for carregada

    return(
        <div>
            <p>Essa é a página HOME USER</p>
            {/* <div style={{width: '100vh', display: 'flex', justifyContent: 'center'}}>Token: {token}</div> */}
        </div>
    )
}