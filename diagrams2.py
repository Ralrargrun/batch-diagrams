import json
from diagrams import Diagram, Cluster
from diagrams.aws.analytics import Glue
from diagrams.aws.compute import Lambda

# Função para mapear os runtimes aos nós correspondentes
def get_node(runtime_type, label):
    if runtime_type == "glue":
        return Glue(label, nodeid=label)
    elif runtime_type == "lambda":
        return Lambda(label, nodeid=label)
    else:
        raise ValueError(f"Tipo de runtime desconhecido: {runtime_type}")

# Leitura do JSON de entrada
with open("dsl.json", "r") as f:
    dsl_data = json.load(f)

steps = dsl_data["schedulerRoutines"][0]["steps"]

# Criação do diagrama
with Diagram("DSL Diagram", show=False, direction="LR", outformat="svg"):
    previous_cluster = None
    total_steps = len(steps)

    for index, step in enumerate(reversed(steps)):
        step_id = step["stepId"]
        tasks = step.get("tasks'", [])
        runtimes = dsl_data["runtimes"]
        i = total_steps - index

        # Criando cluster para cada step
        with Cluster(f"Step {i}:  " + step_id,direction="RL",graph_attr={'margin': "30","fontsize": "20"}):
            nodes = []
            for task in tasks:
                runtime_name = task["runtimeName"]
                task_id = task["taskId"]

                runtime_type = next(runtime["type"] for runtime in runtimes if runtime["name"] == runtime_name)
                node = get_node(runtime_type, task_id)
                nodes.append(node)

            # Disposição horizontal das tasks dentro do cluster
            for i in range(len(nodes) - 1):
                nodes[i] - nodes[i + 1]

        # Conexão entre clusters (opcional, ajustável conforme lógica de dependências)
        # if previous_cluster and nodes:
        #     previous_cluster >> nodes[0]

        previous_cluster = nodes[0] if nodes else None
