from  queue import Queue
from typing import Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #solve using bfs
        rightNode = []
        if root is None:
            return
        
        q = Queue()
        #bfs is done using a queue so we put the root of the binary tree in the q
        q.put(root)


        #keep going untill q is not empty
        while not q.empty():
            #we get the size of the queue to represent how many nodes are on that current level
            levelSize = q.qsize()
            #set the rightmode node to none for later assignement
            rightMostNode = None

            #loop through all the nodes on the level
            for x in range(levelSize):
                #save the current node from the queue inside the var named node
                node=q.get()
                #then set that node to the right side node even though it may be the left one but the last node will always be the
                #rght hand node so that doesnt matter 
                rightMostNode=node.val

                #normal bfs stuff, if the left node of the current node isnt null add it to the queue
                if node.left is not None:
                    q.put(node.left)

                #bfs stuff again if the current right node isnt null add it to the queue
                if node.right is not None:
                    q.put(node.right)

            #add the right most node of the last node to the array of right nodes and return that
            rightNode.append(rightMostNode)
        return rightNode

        
        