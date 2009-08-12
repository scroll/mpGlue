##############################################################
# -----------------------beginHelpText------------------------
# mpGlue  v0.1
# Marin Petrov
# scroll_lock@abv.bg
# http://scroll-lock.eu
# 08.2009
#
#
#
# ------------------------//Usage//---------------------------
# mpGlue constraint - usage is still Null
# 
# 
#
#
# ----------------------//Requires//--------------------------
# 
# 
#
#
# ------------------------//Author//---------------------------
# Marin Petrov;
#
#
# -----------------------endHelpText--------------------------
##############################################################

import math, sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

constraintName = "mpGlue"
nodeId = OpenMaya.MTypeId(0x101118)
print "Import the mpGlue all"

###  mpGlue NODE implementation  ###
class mpGlueNode(OpenMayaMPx.MPxConstraint):
	# constructor for Node
	def __init__(self):
                print "Node __init__"
		OpenMayaMPx.MPxConstraint.__init__(self)
        def compute(self, plug, dataBlock):
                if (plug == mpGlue.constraintGeometry):
                        print "bla"

def nodeCreator():
        return OpenMayaMPx.asMPxPtr( mpGlueNode() )

def nodeInit():
        nAttr = OpenMaya.MFnNumericAttribute()
        uAttr = OpenMaya.MFnUnitAttribute()

        
###  mpGlue COMMAND implementation  ###
class mpGlueCommand(OpenMayaMPx.MPxConstraintCommand):
        # constructor for command #
        def __init__(self):
                print "Command __init__"
                OpenMayaMPx.MPxConstraintCommand.__init__(self)
        def createdConstraint(constraints):
                print "createdConstraint"
        def parseArgs(marglist):
                print "parseArgs"
        def doIt(marglist):
                print "doit"
                
        
def commandCreator():
        print "CommandCreator"
        return OpenMayaMPx.asMPxPtr( mpGlueCommand() )
        
        
###  initialize the command and the node  ###
def initializePlugin(mobject):
        print "enter initialize plugin"
	mplugin = OpenMayaMPx.MFnPlugin(mobject,"Marin Petrov", "0.1", "Any")
	try:
                print "register Node"
		mplugin.registerNode( constraintName, nodeId, nodeCreator ,nodeInit, OpenMayaMPx.MPxConstraint.kConstraintNode )
	except:
		sys.stderr.write( "Failed to register node: %s" % constraintName )
		raise
        try:
                print "register Command"
                mplugin.registerConstraintCommand( constraintName, commandCreator)
	except:
		sys.stderr.write( "Failed to register command: %s" % commandName )
		raise

def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
                print "deregister Node"
		mplugin.deregisterNode( nodeId )
	except:
		sys.stderr.write( "Failed to deregister node: %s" % constraintName )
		raise
        try:
                print "deregister Command"
                mplugin.deregisterConstraintCommand( constraintName )
	except:
		sys.stderr.write( "Failed to deregister command: %s" % commandName )
		raise
                
