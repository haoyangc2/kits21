'''class node():
    def __init__(self, k=None, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r


def create(root):
    a = input('enter a key:')
    if a is '#':
        root = None
    else:
        root = node(k=a)
        root.left = create(root.left)
        root.right = create(root.right)
    return root


def preorder(root):  # 前序遍历
    if root is None:
        return
    else:
        print(root.key)
        preorder(root.left)
        preorder(root.right)


def inorder(root):  # 中序遍历
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


def postorder(root):  # 后序遍历
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.key)


root = None  # 测试代码
root = create(root)
preorder(root)
inorder(root)
postorder(root)'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        pos = root
        while pos:
            if val < pos.val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    print("111")
                    # break
                else:
                    pos = pos.left
            else:
                if not pos.right:
                    pos.right = TreeNode(val)
                    # break
                else:
                    pos = pos.right

        return root
    def listcreattree(self,root,llist,i):###用列表递归创建二叉树，
     #它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
     #再接着创建b的右子树，
     if i<len(llist):
        if llist[i] =='#':
             return None ###这里的return很重要
        else:
             root=TreeNode(llist[i])
             #print('列表序号：'+str(i)+' 二叉树的值：'+str(root.val))
             #往左递推
             root.left=self.listcreattree(root.left,llist,2*i+1)#从根开始一直到最左，直至为空，
           #往右回溯
             root.right=self.listcreattree(root.right, llist,2*i+2)#再返回上一个根，回溯右，
             #再返回根'
             #print('************返回根：',root.val)
             return root  ###这里的return很重要
     return root
llist=[4,2,7,1,3]
a = Solution()
root = a.listcreattree(None,llist,0)
val = 11
print(a.insertIntoBST(root, val))

