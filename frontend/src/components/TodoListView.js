import TodoItem from "./Todo";

const TodoView = (props) => {
  return (
    <div>
      <ul>
        {props.todoList.map((todo, index) => (
          <TodoItem key={index} todo={todo} />
        ))}
      </ul>
    </div>
  );
};

export default TodoView;
