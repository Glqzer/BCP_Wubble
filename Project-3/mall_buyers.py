import frac
import random

class Node:
    
    def __init__(self, id, connected_nodes, minimum_price, fractional_price):
        
        """Parameters:
            id: string to uniquely identify node
            connected_nodes: list of node IDs to which this node has outgoing edges
            minimum_price: Frac object for minimum price
            fractional_price: Frac object for fractional_price
            
            Returns: 
            Creates a Node object"""
            
        self.revenue = frac.Frac(0, 1)
        self.id = id
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        
        return
    
    def add_connectivity(self, node_id):
        
        """Parameters:
            node_id: string to identify node to be connected
            
            Returns: Appends node_id to connected_nodes list"""
        
        self.connected_nodes.append(node_id)
        return
    
    def set_minimum_price(self, price):
        
        """Parameters:
            price: Frac object to represent minimum price
            
            Returns: Changes the minimum price"""
            
        self.minimum_price = price
        return
    
    def set_fractional_price(self, price):
        
        """Parameters:
            price: Frac object to represent fractional price
            
            Returns: Changes the fractional price"""
            
        self.fractional_price = price
        return
    
    
class Buyer:
    
    def __init__(self, current_node_id, remaining_budget):
        
        """Parameters:
            current_node_id: string to indicate which node the buyer current occupies
            remaining_budget: Frac object to represent the amount of money the buyer has left to spend
            
            Returns:
            Creates a Buyer object"""
            
        self.current_node_id = current_node_id
        self.remaining_budget = remaining_budget
        
        return
    
    def create_starting_node(self, node_id_list):
        
        """Parameters:
            node_id_list: list of node_ids to choose from
            
            Returns: sets a starting node for the buyer at random"""
            
        list_length = len(node_id_list)
        id = node_id_list[random.randint(0, list_length - 1)]
        self.current_node_id = id
        return
    
def run_simulation(connectivities_file, building_prices_file, buyer_budget_file):
    
    #Open file for network connectivities
    connectivities_file_read = open(connectivities_file, 'r', encoding='utf-8-sig')
    
    #Create list of connectivities
    list_of_connectivities = []
    for line in connectivities_file_read:
        list_of_connectivities.append(line.split())
    
    connectivities_file_read.close()
    
    #Create list of node IDs (ordered)
    node_ids = []
    
    #Creates list of nodes, ordered same as node ID list
    active_nodes = []
    for line in list_of_connectivities:
        for id in line:
            if id not in node_ids:
                node_ids.append(id)
                active_nodes.append(Node(id, [], frac.Frac(0, 1), frac.Frac(0, 1)))
                
    #Add all the connectivities to the nodes
    for line in list_of_connectivities:
        index = node_ids.index(line[0])
        active_nodes[index].add_connectivity(line[1])
        
    #Open file for pricing schemes
    building_prices_file_read = open(building_prices_file, 'r', encoding='utf-8-sig')
    
    #Create list of building details
    list_of_building_details = []
    for line in building_prices_file_read:
        list_of_building_details.append(line.split())
    
    building_prices_file_read.close()
        
    #Add building details into nodes
    for line in list_of_building_details:
        index = node_ids.index(line[0])
        num = int(line[1])
        den = int(line[2])
        active_nodes[index].set_minimum_price(frac.Frac(num, den))
        num = int(line[3])
        den = int(line[4])
        active_nodes[index].set_fractional_price(frac.Frac(num, den))
        
    #Open file for buyers
    buyer_budget_file_read = open(buyer_budget_file, 'r', encoding='utf-8-sig')
    
    #Create list of connectivities
    for line in buyer_budget_file_read:
        list_of_budgets = line.split()
    
    buyer_budget_file_read.close()
    
    #Create list of buyers
    buyers = []
    for budget in list_of_budgets:
        budget = int(budget)
        buyers.append(Buyer(None, frac.Frac(budget, 1)))
        
    #Start all the buyers at different nodes
    for buyer in buyers:
        buyer.create_starting_node(node_ids)
    
    #Actually run the simulation now
    full_total_revenue = frac.Frac(0, 1)
    for buyer in buyers:
        while True:
            
            #Find current node
            node_index = node_ids.index(buyer.current_node_id)
            current_node = active_nodes[node_index]
            
            #Test current node buy
            if (current_node.minimum_price > buyer.remaining_budget):
                break
            
            #Buy and adjust values
            price_paid = buyer.remaining_budget * current_node.fractional_price
            buyer.remaining_budget = buyer.remaining_budget - price_paid
            current_node.revenue = current_node.revenue + price_paid
            full_total_revenue = full_total_revenue + price_paid
            
            #Move onto next node
            list_len = len(current_node.connected_nodes)
            id = current_node.connected_nodes[random.randint(0, list_len - 1)]
            buyer.current_node_id = id
    
    result_dict = {}
    for node in active_nodes:
        value = node.revenue / full_total_revenue 
        key = node.id
        dict[key] = value        
        
    return full_total_revenue and result_dict
