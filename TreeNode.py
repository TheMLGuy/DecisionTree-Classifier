class TreeNode:
    value = ""
    children = []
    
    def __init__(self, val, dictionary):
        self.setValue(val)
        self.getChildren(dictionary)
    
    def __str__(self):
        return str(self.value)
    
    def setValue(self, val):
        self.value = val
        
    def getChildren(self, dictionary):
        if(isinstance(dictionary, dict)):
            self.children = dictionary.keys()
    
    