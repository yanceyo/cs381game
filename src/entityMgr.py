from vector import Vector3
import ogre.renderer.OGRE as ogre

Quaternion = ogre.Quaternion

class EntityMgr:
    def __init__(self, engine):
        print "starting ent mgr"
        self.engine = engine
                
    def init(self):
        self.ents = {}
        self.nEnts = 0
        import ent
        self.entTypes = [ent.PlayerShip, ent.EnemyShip,]
        
        self.playerObject = None

    def createEnt(self, entType, pos = Vector3(0,0,0), orientation = Quaternion(0,0,0,1)):
        ent = entType(self.engine, self.nEnts, pos = pos, orientation = orientation)
        print "EntMgr created: ", ent.uiname, ent.eid, self.nEnts
        ent.init()
        self.ents[self.nEnts] = ent;
        self.nEnts = self.nEnts + 1
        
        if ent.isPlayerControlled:
            self.playerObject = ent
        
        return ent

    def tick(self, dt):
        for eid, ent in self.ents.iteritems():
            ent.tick(dt)
        

