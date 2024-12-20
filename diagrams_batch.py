from diagrams import Cluster,Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.analytics import Glue
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=False, direction="TB", outformat="svg"):
    
    with Cluster("Step 1",graph_attr={'margin': "30"}):
       glue1 = Glue("hsuadhususahdusahdu",nodeid="xablau",href="xablau", target="_blank") 
       glue2 = Glue("hsuadhususahdusahdu",nodeid="xablau2",href="xablau", target="_blank") 

    with Cluster("Step 2",graph_attr={'margin': "30"}):
       glue3 = Glue("hsuadhususahdusahdu",nodeid="xablau3",href="xablau", target="_blank") 
       glue4 = Glue("hsuadhususahdusahdu",nodeid="xablau4",href="xablau", target="_blank") 
       glue5 = Glue("hsuadhususahdusahdu",nodeid="xablau5",href="xablau", target="_blank") 
       glue6 = Glue("hsuadhususahdusahdu",nodeid="xablau6",href="xablau", target="_blank") 
       glue7 = Glue("hsuadhususahdusahdu",nodeid="xablau7",href="xablau", target="_blank") 
       glue8 = Glue("hsuadhususahdusahdu",nodeid="xablau8",href="xablau", target="_blank") 
    
    glue1 >> glue3