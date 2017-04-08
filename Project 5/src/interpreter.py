from env import GlobalEnv, LocalEnv

genv = GlobalEnv.empty_env()
result = 0


def eval_tree(tree):
    """ The top level function.
        Args:
            tree (ast.Module): The ast abstract syntax tree- the root is a Module node object. The children are contained in a list.
        Returns:
            integer or float: the result of any value returned by the program, 0 by default.
    """
    global genv
    global result
    # Here, get the list of children nodes. Iterate over that list, calling eval_node on each node.
    return result


def node_name(node):
    return type(node).__name__


def eval_node(node, env):
    """ Evaluates a Node object in the abstract syntax tree.
        Args:
            node (ast.Node): The node to evaluate.
            env (GlobalEnv | LocalEnv): An environment data type.
        Returns:
            (integer or float, environment): A tuple, where the first element is the result of any
            value computed at this node, and the second value is either a GlobalEnv or LocalEnv object.
    """
    global genv
    global result
    node_type = node_name(node)
    if node_type == 'Expr':
        return eval_node(node.value, env)
    elif node_type == 'Assign':
        # extract the variable name, evaluate the RHS, then extend the environment.
        return 0, env
    elif node_type == 'BinOp':
        # get the left and right operands (we use only single operands) and the operator.
        # evaluate the operands and apply the operator. return the number, env.
        return 0, env
    elif node_type == 'FunctionDef':
        # need the function id (name), args, and body. Extend the environment.
        # you can leave the args wrapped in the ast class and the body and unpack them
        # when the function is called.
        return 0, env
    elif node_type == 'Call':
        # get any values passed in to the function from the Call object.
        # get the fxn name and look up its parameters, if any, and body from the env.
        # get lists for parameter names and values and extend a LocalEnv with those bindings.
        # evaluate the body in the local env, return the value, env.
        return 0, env
    elif node_type == 'Return':
        # evaluate the node, return the value, env.
        return 0, env
    elif node_type == 'Name':
        # Name(identifier id)- lookup the value binding in the env
        # return the value, env
        return 0, env
    # Num(object n) -- a number, return the number, env.
    elif node_type == 'Num':
        return node.n, env
