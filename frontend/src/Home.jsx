import { useState,useEffect } from "react";
import api from "./api";
import Note from "./components/Note";
export default function Home(){
    const [tasks,setTasks]=useState([]);
    const [title,setTitle]=useState("");

    useEffect(()=>{
        getTasks();
    },[])

    const getTasks=()=>{
        api.get('/api/tasks/').then((res)=>res.data).then((data)=>{
            setTasks(data);
            console.log(data);
        }).catch((err)=>alert(err));
    };

    const createTask=(e)=>{
        e.preventDefault();
        api.post('/api/tasks/',{title}).then((res)=>{
            if(res.status===201) {alert("New Task Added");
                setTitle("")
            }
            else alert("Failed to creat Task");
            getTasks();
        }).catch((err)=>{
            alert(err);
        });
    };

    const deleteTask=(id)=>{
        api.delete(`/api/tasks/update/${id}/`).then((res)=>{
            if(res.status===204) alert ("Task Deleted");
            getTasks();
        }).catch((err)=>alert(err));
    };

    const toggleTask= async (taskId,CurrentStatus)=>{
        const task=tasks.find(t=>t.id===taskId);
        try{
            await api.patch(`/api/tasks/update/${taskId}/`,
            {completed:!CurrentStatus});
            getTasks();
        }catch(err){
            console.error(err);
        }
    };

    return (
        <div>
            <div>
                <form onSubmit={createTask}>
                    <input type="text" 
                    placeholder="Add new Task"
                    value={title}
                    onChange={(e)=>setTitle(e.target.value)}
                    required
                    />
                    <button type="submit">Add</button>
                </form>
                <h2>My Tasks</h2>
                {tasks.length?
                (tasks.map((task)=>
              <div key={task.id}>
                <p>{task.title}</p>
                <input type="checkbox" checked={task.completed} onChange={()=>toggleTask(task.id,task.completed)} />
                <button onClick={()=>deleteTask(task.id)}>Delete</button>
              </div>
                ))
                :<p> No task Added </p>}
            </div>
        </div>

    )
}