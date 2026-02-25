import React, { useEffect, useState } from "react"
import axios from "axios"

export default function HomeUser() {
    const [user, setUser] = useState([])
    const [password, setPassword] = useState('')
    const [nome, setNome] = useState('')
    const [tipo, setTipo] = useState('')

    const token = localStorage.getItem('token')

    const listar = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/usuarios', {
                headers: { Authorization: `Bearer ${token}` },
                params: {
                    nome: nome,
                    tipo: tipo
                }
            })
            setUser(response.data)
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => { listar() }, [])

    return (
        <div>
            <h2>Lista de Usuários</h2>

            <div style={{ marginBottom: "20px" }}>
                <input
                    type="text"
                    placeholder="Filtrar por nome..."
                    value={nome}
                    onChange={(e) => setNome(e.target.value)}
                    style={{ marginRight: "10px", padding: "5px" }}
                />

                <select
                    value={tipo}
                    onChange={(e) => setTipo(e.target.value)}
                    style={{ marginRight: "10px", padding: "5px" }}
                >
                    <option value="">Todos os tipos</option>
                    <option value="LOCADOR">Locador</option>
                    <option value="LOCATARIO">Locatario</option>
                </select>

                <button onClick={listar} style={{ padding: "5px 15px" }}>
                    Filtrar
                </button>
            </div>
            {/*Tabela principal */}
            <table border="1" cellPadding="6" style={{ width: "100%" }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {user.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <hr style={{ margin: "20px 0" }} />
        </div>
    )
}