from CvPythonExtensions import *
import time
import math
import operator
import CvCameraControls
import MercenaryUtils # koma13
import Popup as PyPopup
import CvUtil
import BugUtil
import BugData
import CvReligionScreen
import CvMiscScreen

gc = CyGlobalContext()
DuneWarsInst = ""
objMercenaryUtils = MercenaryUtils.MercenaryUtils() #koma13

#!M! -> many changes, corrections and more efficiency

# Entry points from CvGameUtils.  If you add one, update config/init.xml
def AI_unitUpdate(argsList):
        return DuneWarsInst.AI_unitUpdate(argsList[0])

def getWidgetHelp(argsList):
	eWidgetType, iData1, iData2, bOption = argsList
	if iData1 == 667: 
		return CyTranslator().getText("TXT_KEY_HW_VERSION", ())
	
## Platy WorldBuilder ##
        elif eWidgetType == WidgetTypes.WIDGET_PYTHON:
                if iData1 == 1027:
                        return CyTranslator().getText("TXT_KEY_WB_PLOT_DATA",())
                elif iData1 == 1028:
                        return gc.getGameOptionInfo(iData2).getHelp()
                elif iData1 == 1029:
                        if iData2 == 0:
                                sText = CyTranslator().getText("TXT_KEY_WB_PYTHON", ())
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onFirstContact"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onChangeWar"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onVassalState"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onCityAcquired"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onCityBuilt"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onCultureExpansion"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onGoldenAge"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onEndGoldenAge"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onGreatPersonBorn"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onPlayerChangeStateReligion"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onReligionFounded"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onReligionSpread"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onReligionRemove"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onCorporationFounded"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onCorporationSpread"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onCorporationRemove"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onUnitCreated"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onUnitLost"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onUnitPromoted"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onBuildingBuilt"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onProjectBuilt"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onTechAcquired"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onImprovementBuilt"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onImprovementDestroyed"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onRouteBuilt"
                                sText += "\n" + CyTranslator().getText("[ICON_BULLET]", ()) + "onPlotRevealed"
                                return sText
                        elif iData2 == 1:
                                return CyTranslator().getText("TXT_KEY_WB_PLAYER_DATA",())
                        elif iData2 == 2:
                                return CyTranslator().getText("TXT_KEY_WB_TEAM_DATA",())
                        elif iData2 == 3:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_TECH",())
                        elif iData2 == 4:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_PROJECT",())
                        elif iData2 == 5:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_UNIT", ()) + " + " + CyTranslator().getText("TXT_KEY_CONCEPT_CITIES", ())
                        elif iData2 == 6:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_PROMOTION",())
                        elif iData2 == 7:
                                return CyTranslator().getText("TXT_KEY_WB_CITY_DATA2",())
                        elif iData2 == 8:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_BUILDING",())
                        elif iData2 == 9:
                                return "Platy Builder\nVersion: 4.17b"
                        elif iData2 == 10:
                                return CyTranslator().getText("TXT_KEY_CONCEPT_EVENTS",())
                        elif iData2 == 11:
                                return CyTranslator().getText("TXT_KEY_WB_RIVER_PLACEMENT",())
                        elif iData2 == 12:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_IMPROVEMENT",())
                        elif iData2 == 13:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_BONUS",())
                        elif iData2 == 14:
                                return CyTranslator().getText("TXT_KEY_WB_PLOT_TYPE",())
                        elif iData2 == 15:
                                return CyTranslator().getText("TXT_KEY_CONCEPT_TERRAIN",())
                        elif iData2 == 16:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_ROUTE",())
                        elif iData2 == 17:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_FEATURE",())
                        elif iData2 == 18:
                                return CyTranslator().getText("TXT_KEY_MISSION_BUILD_CITY",())
                        elif iData2 == 19:
                                return CyTranslator().getText("TXT_KEY_WB_ADD_BUILDINGS",())
                        elif iData2 == 20:
                                return CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_RELIGION",())
                        elif iData2 == 21:
                                return CyTranslator().getText("TXT_KEY_CONCEPT_CORPORATIONS",())
                        elif iData2 == 22:
                                return CyTranslator().getText("TXT_KEY_ESPIONAGE_CULTURE",())
                        elif iData2 == 23:
                                return CyTranslator().getText("TXT_KEY_PITBOSS_GAME_OPTIONS",())
                        elif iData2 == 24:
                                return CyTranslator().getText("TXT_KEY_WB_SENSIBILITY",())
                        elif iData2 == 27:
                                return CyTranslator().getText("TXT_KEY_WB_ADD_UNITS",())
                        elif iData2 == 28:
                                return CyTranslator().getText("TXT_KEY_WB_TERRITORY",())
                        elif iData2 == 29:
                                return CyTranslator().getText("TXT_KEY_WB_ERASE_ALL_PLOTS",())
                        elif iData2 == 30:
                                return CyTranslator().getText("TXT_KEY_WB_REPEATABLE",())
                        elif iData2 == 31:
                                return CyTranslator().getText("TXT_KEY_PEDIA_HIDE_INACTIVE", ())
                        elif iData2 == 32:
                                return CyTranslator().getText("TXT_KEY_WB_STARTING_PLOT", ())
                        elif iData2 == 33:
                                return CyTranslator().getText("TXT_KEY_INFO_SCREEN", ())
                        elif iData2 == 34:
                                return CyTranslator().getText("TXT_KEY_CONCEPT_TRADE", ())
                elif iData1 > 1029 and iData1 < 1040:
                        if iData1 %2:
                                return "-"
                        return "+"
                elif iData1 == 1041:
                        return CyTranslator().getText("TXT_KEY_WB_KILL",())
                elif iData1 == 1042:
                        return CyTranslator().getText("TXT_KEY_MISSION_SKIP",())
                elif iData1 == 1043:
                        if iData2 == 0:
                                return CyTranslator().getText("TXT_KEY_WB_DONE",())
                        elif iData2 == 1:
                                return CyTranslator().getText("TXT_KEY_WB_FORTIFY",())
                        elif iData2 == 2:
                                return CyTranslator().getText("TXT_KEY_WB_WAIT",())
                elif iData1 == 6785:
                        return CyGameTextMgr().getProjectHelp(iData2, False, CyCity())
                elif iData1 == 6787:
                        return gc.getProcessInfo(iData2).getDescription()
                elif iData1 == 6788:
                        if iData2 == -1:
                                return CyTranslator().getText("TXT_KEY_CULTURELEVEL_NONE", ())
                        return gc.getRouteInfo(iData2).getDescription()
## City Hover Text ##
                elif iData1 > 7199 and iData1 < 7300:
                        iPlayer = iData1 - 7200
                        pPlayer = gc.getPlayer(iPlayer)
                        pCity = pPlayer.getCity(iData2)
                        if CyGame().GetWorldBuilderMode():
                                sText = "<font=3>"
                                if pCity.isCapital():
                                        sText += CyTranslator().getText("[ICON_STAR]", ())
                                elif pCity.isGovernmentCenter():
                                        sText += CyTranslator().getText("[ICON_SILVER_STAR]", ())
                                sText += u"%s: %d<font=2>" %(pCity.getName(), pCity.getPopulation())
                                sTemp = ""
                                if pCity.isConnectedToCapital(iPlayer):
                                        sTemp += CyTranslator().getText("[ICON_TRADE]", ())
                                for i in xrange(gc.getNumReligionInfos()):
                                        if pCity.isHolyCityByType(i):
                                                sTemp += u"%c" %(gc.getReligionInfo(i).getHolyCityChar())
                                        elif pCity.isHasReligion(i):
                                                sTemp += u"%c" %(gc.getReligionInfo(i).getChar())

                                for i in xrange(gc.getNumCorporationInfos()):
                                        if pCity.isHeadquartersByType(i):
                                                sTemp += u"%c" %(gc.getCorporationInfo(i).getHeadquarterChar())
                                        elif pCity.isHasCorporation(i):
                                                sTemp += u"%c" %(gc.getCorporationInfo(i).getChar())
                                if len(sTemp) > 0:
                                        sText += "\n" + sTemp

                                iMaxDefense = pCity.getTotalDefense(False)
                                if iMaxDefense > 0:
                                        sText += u"\n%s: " %(CyTranslator().getText("[ICON_DEFENSE]", ()))
                                        iCurrent = pCity.getDefenseModifier(False)
                                        if iCurrent != iMaxDefense:
                                                sText += u"%d/" %(iCurrent)
                                        sText += u"%d%%" %(iMaxDefense)

                                sText += u"\n%s: %d/%d" %(CyTranslator().getText("[ICON_FOOD]", ()), pCity.getFood(), pCity.growthThreshold())
                                iFoodGrowth = pCity.foodDifference(True)
                                if iFoodGrowth != 0:
                                        sText += u" %+d" %(iFoodGrowth)

                                if pCity.isProduction():
                                        sText += u"\n%s:" %(CyTranslator().getText("[ICON_PRODUCTION]", ()))
                                        if not pCity.isProductionProcess():
                                                sText += u" %d/%d" %(pCity.getProduction(), pCity.getProductionNeeded())
                                                iProduction = pCity.getCurrentProductionDifference(False, True)
                                                if iProduction != 0:
                                                        sText += u" %+d" %(iProduction)
                                        sText += u" (%s)" %(pCity.getProductionName())

                                iGPRate = pCity.getGreatPeopleRate()
                                iProgress = pCity.getGreatPeopleProgress()
                                if iGPRate > 0 or iProgress > 0:
                                        sText += u"\n%s: %d/%d %+d" %(CyTranslator().getText("[ICON_GREATPEOPLE]", ()), iProgress, pPlayer.greatPeopleThreshold(False), iGPRate)

                                sText += u"\n%s: %d/%d (%s)" %(CyTranslator().getText("[ICON_CULTURE]", ()), pCity.getCulture(iPlayer), pCity.getCultureThreshold(), gc.getCultureLevelInfo(pCity.getCultureLevel()).getDescription())

                                lTemp = []
                                for i in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
                                        iAmount = pCity.getCommerceRateTimes100(i)
                                        if iAmount <= 0: continue
                                        sTemp = u"%d.%02d%c" %(pCity.getCommerceRate(i), pCity.getCommerceRateTimes100(i)%100, gc.getCommerceInfo(i).getChar())
                                        lTemp.append(sTemp)
                                if len(lTemp) > 0:
                                        sText += "\n"
                                        for i in xrange(len(lTemp)):
                                                sText += lTemp[i]
                                                if i < len(lTemp) - 1:
                                                        sText += ", "

                                iMaintenance = pCity.getMaintenanceTimes100()
                                if iMaintenance != 0:
                                        sText += "\n" + CyTranslator().getText("[COLOR_WARNING_TEXT]", ()) + CyTranslator().getText("INTERFACE_CITY_MAINTENANCE", ()) + " </color>"
                                        sText += u"-%d.%02d%c" %(iMaintenance/100, iMaintenance%100, gc.getCommerceInfo(CommerceTypes.COMMERCE_GOLD).getChar())

                                lBuildings = []
                                lWonders = []
                                for i in xrange(gc.getNumBuildingInfos()):
                                        if pCity.isHasBuilding(i):
                                                Info = gc.getBuildingInfo(i)
                                                if isLimitedWonderClass(Info.getBuildingClassType()):
                                                        lWonders.append(Info.getDescription())
                                                else:
                                                        lBuildings.append(Info.getDescription())
                                if len(lBuildings) > 0:
                                        lBuildings.sort()
                                        sText += "\n" + CyTranslator().getText("[COLOR_BUILDING_TEXT]", ()) + CyTranslator().getText("TXT_KEY_PEDIA_CATEGORY_BUILDING", ()) + ": </color>"
                                        for i in xrange(len(lBuildings)):
                                                sText += lBuildings[i]
                                                if i < len(lBuildings) - 1:
                                                        sText += ", "
                                if len(lWonders) > 0:
                                        lWonders.sort()
                                        sText += "\n" + CyTranslator().getText("[COLOR_SELECTED_TEXT]", ()) + CyTranslator().getText("TXT_KEY_CONCEPT_WONDERS", ()) + ": </color>"
                                        for i in xrange(len(lWonders)):
                                                sText += lWonders[i]
                                                if i < len(lWonders) - 1:
                                                        sText += ", "
                                sText += "</font>"
                                return sText
## Religion Widget Text##
                elif iData1 == 7869:
                        return CyGameTextMgr().parseReligionInfo(iData2, False)
## Building Widget Text##
                elif iData1 == 7870:
                        return CyGameTextMgr().getBuildingHelp(iData2, False, False, False, None)
## Tech Widget Text##
                elif iData1 == 7871:
                        if iData2 == -1:
                                return CyTranslator().getText("TXT_KEY_CULTURELEVEL_NONE", ())
                        return CyGameTextMgr().getTechHelp(iData2, False, False, False, False, -1)
## Civilization Widget Text##
                elif iData1 == 7872:
                        iCiv = iData2 % 10000
                        return CyGameTextMgr().parseCivInfos(iCiv, False)
## Promotion Widget Text##
                elif iData1 == 7873:
                        return CyGameTextMgr().getPromotionHelp(iData2, False)
## Feature Widget Text##
                elif iData1 == 7874:
                        if iData2 == -1:
                                return CyTranslator().getText("TXT_KEY_CULTURELEVEL_NONE", ())
                        iFeature = iData2 % 10000
                        return CyGameTextMgr().getFeatureHelp(iFeature, False)
## Terrain Widget Text##
                elif iData1 == 7875:
                        return CyGameTextMgr().getTerrainHelp(iData2, False)
## Leader Widget Text##
                elif iData1 == 7876:
                        iLeader = iData2 % 10000
                        return CyGameTextMgr().parseLeaderTraits(iLeader, -1, False, False)
## Improvement Widget Text##
                elif iData1 == 7877:
                        if iData2 == -1:
                                return CyTranslator().getText("TXT_KEY_CULTURELEVEL_NONE", ())
                        return CyGameTextMgr().getImprovementHelp(iData2, False)
## Bonus Widget Text##
                elif iData1 == 7878:
                        if iData2 == -1:
                                return CyTranslator().getText("TXT_KEY_CULTURELEVEL_NONE", ())
                        return CyGameTextMgr().getBonusHelp(iData2, False)
## Specialist Widget Text##
                elif iData1 == 7879:
                        try:
                                return CyGameTextMgr().getSpecialistHelp(iData2, False)
                        except: pass
## Yield Text##
                elif iData1 == 7880:
                        return gc.getYieldInfo(iData2).getDescription()
## Commerce Text##
                elif iData1 == 7881:
                        return gc.getCommerceInfo(iData2).getDescription()
## Build Text##
                elif iData1 == 7882:
                        return gc.getBuildInfo(iData2).getDescription()
## Corporation Screen ##
                elif iData1 == 8201:
                        return CyGameTextMgr().parseCorporationInfo(iData2, False)
## Military Screen ##
                elif iData1 == 8202:
                        if iData2 == -1:
                                return CyTranslator().getText("TXT_KEY_PEDIA_ALL_UNITS", ())
                        return CyGameTextMgr().getUnitHelp(iData2, False, False, False, None)
                elif iData1 > 8299 and iData1 < 8400:
                        iPlayer = iData1 - 8300
                        pUnit = gc.getPlayer(iPlayer).getUnit(iData2)
                        sText = CyGameTextMgr().getSpecificUnitHelp(pUnit, True, False)
                        if CyGame().GetWorldBuilderMode():
                                sText += "\n" + CyTranslator().getText("TXT_KEY_WB_UNIT", ()) + " ID: " + str(iData2)
                                sText += "\n" + CyTranslator().getText("TXT_KEY_WB_GROUP", ()) + " ID: " + str(pUnit.getGroupID())
                                sText += "\n" + "X: " + str(pUnit.getX()) + ", Y: " + str(pUnit.getY())
                                sText += "\n" + CyTranslator().getText("TXT_KEY_WB_AREA_ID", ()) + ": "  + str(pUnit.plot().getArea())
                        return sText
## Civics Screen ##
                elif iData1 == 8205 or iData1 == 8206:
                        sText = CyGameTextMgr().parseCivicInfo(iData2, False, True, False)
                        if gc.getCivicInfo(iData2).getUpkeep() > -1:
                                sText += "\n" + gc.getUpkeepInfo(gc.getCivicInfo(iData2).getUpkeep()).getDescription()
                        else:
                                sText += "\n" + CyTranslator().getText("TXT_KEY_CIVICS_SCREEN_NO_UPKEEP", ())
                        return sText
## End Platy WorldBuilder ##
                
        # !M! ->
        elif eWidgetType == WidgetTypes.WIDGET_GENERAL:
                # Inquisition:
                if iData1 == 8586:
                        return CyTranslator().getText("TXT_KEY_PURGE_RELIGION",(gc.getReligionInfo(iData2).getDescription(),))
                #Mentat
                elif iData1 == 4455:
                        sMentatQuality = gc.getBuildingInfo(iData2).getType()
                        sMentatQuality = sMentatQuality.replace("BUILDING_", "PROMOTION_")
                        return CyTranslator().getText("TXT_KEY_MENTAT_ASSIGN",()) + CyGameTextMgr().getPromotionHelp(gc.getInfoTypeForString(sMentatQuality), False)
                #Tleilaxu Gholas:
                elif iData1 == 8999:
                        SD_MOD_ID = "GeneticDataID: " + str(CyGame().getActivePlayer())
                        UNITS_DATA = "UnitsData" 
                        GeneticData = BugData.getGameData().getTable(SD_MOD_ID)
                        UnitsData = GeneticData[UNITS_DATA]
                        sPromos = ""
                        for i in UnitsData[iData2]["Promotions"]:
                                sPromos += (CyTranslator().getText("[ICON_SILVER_STAR]", ()) + gc.getPromotionInfo(i).getDescription() + " ")
                        sName = UnitsData[iData2]["Name"]
                        iExp = (UnitsData[iData2]["Exp"] / 10)
                        iLevel = UnitsData[iData2]["Level"]
                        iCost = gc.getUnitInfo(UnitsData[iData2]["UnitType"]).getProductionCost()
                        return CyTranslator().getText("TXT_KEY_TLEILAX_GHOLA_SELECT", (sName, sPromos, iExp, iLevel, iCost))
                elif iData1 == 1321:
                        return "Select the Ghola and jump to its location"
                elif iData1 == 1232:
                        return CyGameTextMgr().getPromotionHelp(iData2, False)
                elif iData1 == 1233:
                        return CyGameTextMgr().getUnitHelp(iData2, False, False, False, None)
                elif iData1 == 1235:
                        SD_MOD_ID = "GeneticDataID: " + str(CyGame().getActivePlayer())
                        UNITS_DATA = "UnitsData" 
                        GeneticData = BugData.getGameData().getTable(SD_MOD_ID)
                        UnitsData = GeneticData[UNITS_DATA]
                        sPromos = CyTranslator().getText("[ICON_BULLET]Additional Promotions:", ())
                        sPromos2 = CyTranslator().getText("[ICON_BULLET]Additional Promotions:[NEWLINE]", ())
                        iCountPromos = 0
                        for i in UnitsData[iData2]["Promotions"]:
                                iCountPromos += 1
                                if iCountPromos > 11:
                                        sPromos += CyTranslator().getText("[NEWLINE][NEWLINE][ICON_SILVER_STAR][SPACE]", ()) + CyGameTextMgr().getPromotionHelp(i, False)
                                        sPromos2 += CyTranslator().getText("[NEWLINE][ICON_SILVER_STAR][SPACE]%s1", (gc.getPromotionInfo(i).getDescription(),))
                        if iCountPromos < 16:
                                return sPromos
                        else:
                                return sPromos2
                #Axlotl Bonus:
                elif iData1 == 8123:
                        SD_MOD_ID = "AxlotlGPBonusID: " + str(CyGame().getActivePlayer())
                        SP_KILL_COUNT = "Assassinations"
                        if (not BugData.getGameData().getTable(SD_MOD_ID).hasTable(SP_KILL_COUNT)):
                                AxlotlBonus = BugData.getGameData().getTable(SD_MOD_ID)
                                AxlotlBonus[SP_KILL_COUNT] = 0
                        AxlotlBonus = BugData.getGameData().getTable(SD_MOD_ID)
                        iTotal = AxlotlBonus[SP_KILL_COUNT] + iData2
                        if iTotal > 0:
                                return CyTranslator().getText("TXT_AXLOTL_BONUS", (AxlotlBonus[SP_KILL_COUNT], iData2, iTotal))
                        else:
                                return " This city's Axlotl Chamber is awaiting specimens for potential Great Person experiments."
                elif iData1 == 3456:
                        return "No sufficient 'Genetic Models' available."
                #Religious Advisor:
                elif iData1 == 1446:
                        pPlayer = gc.getPlayer(CyGame().getActivePlayer())
                        pCity = pPlayer.getCity(iData2)
                        sHelp = CyTranslator().getText("[ICON_BULLET]Additional [ICON_RELIGION] Buildings in the City:", ())
                        sHelp2 = CyTranslator().getText("[ICON_BULLET]Additional [ICON_RELIGION] Buildings in the City:[NEWLINE]", ())
                        iCountBldg = 0
                        for iBldg in xrange(gc.getNumBuildingInfos()):
                                if gc.getBuildingInfo(iBldg).getReligionType() > -1:
                                        if pCity.getNumBuilding(iBldg) > 0:
                                                iCountBldg += 1
                                                if iCountBldg > 10:
                                                        sHelp += CyTranslator().getText("[NEWLINE][NEWLINE][ICON_RELIGION][SPACE]", ()) + CyGameTextMgr().getBuildingHelp(iBldg, False, False, False, None)
                                                        sHelp2 += CyTranslator().getText("[NEWLINE][ICON_RELIGION][SPACE]%s1", (gc.getBuildingInfo(iBldg).getDescription(),))
                        if iCountBldg < 16:
                                return sHelp
                        else:
                                return sHelp2
                elif iData1 >= 5999 and iData1 <= 6006:
                        sHelp = CvReligionScreen.CvReligionScreen().EnhancedEffects(iData1 - 6000, iData2)#iReligion, iCityID
                        return sHelp
                        
	return u""

# Entry points from CvRandomEventsInterface.py

def ContractCan(argsList, sType):
	return DuneWarsInst.ContractCan(argsList, sType)
def ContractDo(argsList, sType):
	return DuneWarsInst.ContractDo(argsList, sType)
def ContractHelp(argsList, sType):
	return DuneWarsInst.ContractHelp(argsList, sType)
def MentatDo(argsList, sType):
	return DuneWarsInst.MentatDo(argsList, sType)
def MentatHelp(argsList, sType):
	return DuneWarsInst.MentatHelp(argsList, sType)
# Abomination Trait
def AbominationDo(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	for i in xrange(gc.getNumTraitInfos()):
		if (pPlayer.hasTrait(i) and i != gc.getInfoTypeForString('TRAIT_ABOMINATION')):
			pPlayer.setHasTrait(i, False)
	Traits = [ 'TRAIT_AGGRESSIVE','TRAIT_CHARISMATIC','TRAIT_CREATIVE','TRAIT_EXPANSIVE','TRAIT_FINANCIAL','TRAIT_INDUSTRIOUS','TRAIT_ORGANIZED','TRAIT_PHILOSOPHICAL','TRAIT_SPIRITUAL' ]
	iRnd1 = CyGame().getSorenRandNum(len(Traits), "Abomination")
	iRnd2 = CyGame().getSorenRandNum(len(Traits), "Abomination")
	while iRnd2 == iRnd1:
		iRnd2 = CyGame().getSorenRandNum(len(Traits), "Abomination")
	pPlayer.setHasTrait(gc.getInfoTypeForString(Traits[iRnd1]),True)
	pPlayer.setHasTrait(gc.getInfoTypeForString(Traits[iRnd2]),True)
	
# Entry points from CvMainInterface.py
def StormDraw():
	DuneWarsInst.StormDraw()

# Entry points from CvVictoryScreen.py
def TerraVictoryPlots():
	return DuneWarsInst.TerraVictoryPlots()
def TerraVictoryPlayer(iTeam):
	return DuneWarsInst.TerraVictoryPlayer(iTeam)
def SpiceVictoryRequiredBonuses():
	return DuneWarsInst.SpiceVictoryRequiredBonuses()
def SpiceVictoryFixedAmount():
	return DuneWarsInst.SpiceVictoryFixedAmount()
def SpiceVictoryGetPercentage():
	return DuneWarsInst.SpiceVictoryGetPercentage()
def SpiceVictoryPlayer(iTeam):
	return DuneWarsInst.SpiceVictoryPlayer(iTeam)


class DuneWars:
	### PUBLIC ENTRY POINTS
	# Initialize, called from BUG init
	def __init__(self, customEM, configfile):
		global DuneWarsInst
		self.bInitialized = false
		DuneWarsInst = self
		# Event handlers		
		customEM.addEventHandler("ModNetMessage", self.onModNetMessage)
		customEM.addEventHandler("EndGameTurn", self.onEndGameTurn)
		customEM.addEventHandler("BeginPlayerTurn", self.onBeginPlayerTurn)
		customEM.addEventHandler("GameStart", self.onGameStart)
		customEM.addEventHandler("OnLoad", self.onGameLoad)
		customEM.addEventHandler("PythonReloaded", self.onGameLoad)
		customEM.addEventHandler("cityBuilt", self.onCityBuilt)
		customEM.addEventHandler("cityAcquired", self.onCityAcquired)
		customEM.addEventHandler("religionSpread", self.onReligionSpread)

		# Shortcut keys for camera control
		customEM.addShortcutHandler("shift left", self.CameraSL)
		customEM.addShortcutHandler("ctrl left", self.CameraCL)
		customEM.addShortcutHandler("shift right", self.CameraSR)
		customEM.addShortcutHandler("ctrl right", self.CameraCR)
		customEM.addShortcutHandler("shift up", self.CameraSCU)
		customEM.addShortcutHandler("ctrl up", self.CameraSCU)
		customEM.addShortcutHandler("shift down", self.CameraSCD)
		customEM.addShortcutHandler("ctrl down", self.CameraSCD)
		customEM.addShortcutHandler("ctrl home", self.CameraCH)
		
	# AI movement (!M! -> only called for the below unit)
	def AI_unitUpdate(self, pUnit):
		self.Initialize()
                if pUnit.getUnitType() == self.iUGhola:
                        iPlayer = pUnit.getOwner(); pPlayer = gc.getPlayer(iPlayer); pTeam = gc.getTeam(pPlayer.getTeam())
                        SD_MOD_ID = "GeneticDataID: " + str(iPlayer)
                        UNITS_DATA = "UnitsData"
                        if (not BugData.getGameData().getTable(SD_MOD_ID).hasTable(UNITS_DATA)): return false
                        GeneticData = BugData.getGameData().getTable(SD_MOD_ID)
                        UnitsData = GeneticData[UNITS_DATA]
                        iModel = -1; iBestExp = 0
                        
                        for id in UnitsData:
                                pGeneticModel = pPlayer.getUnit(UnitsData[id]["GholaID"])
                                if pGeneticModel.isNone():
                                        iUnit = UnitsData[id]["UnitType"]
                                        if pPlayer.getGold() > gc.getUnitInfo(iUnit).getProductionCost():
                                                bCheckExp = False
                                                UnitInfo = gc.getUnitInfo(iUnit)
                                                if not UnitInfo.getUnitCombatType() == UnitCombatTypes.MELEE_COMBAT:
                                                        if pTeam.isHasTech(UnitInfo.getPrereqAndTech()):
                                                                iPreReqBonus = UnitInfo.getPrereqAndBonus()
                                                                if iPreReqBonus > -1:
                                                                        pPlot = pUnit.plot()
                                                                        if pPlot.isCity():
                                                                                if pPlot.getPlotCity().hasBonus(iPreReqBonus):
                                                                                        bCheckExp = True
                                                                else:
                                                                        bCheckExp = True
                                                else:
                                                        bCheckExp = True
                                                if bCheckExp:
                                                        if UnitsData[id]["Exp"] > iBestExp:
                                                                iBestExp = UnitsData[id]["Exp"]
                                                                iModel = id
                        if iModel > -1:
                                self.TleilaxuGhola(pUnit.getOwner(), pUnit.getID(), iModel)
                                return true
                return false

### CAMERA CONTROL
	def CameraCL(self, argsList):
		CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() - 45.0)
	def CameraSL(self, argsList):
		CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() - 15.0)
	def CameraCR(self, argsList):
		CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() + 45.0)
	def CameraSR(self, argsList):
		CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() + 15.0)
	def CameraSCU(self, argsList):
		if CyCamera().GetBasePitch() > -45:
			CyCamera().SetBasePitch(CyCamera().GetBasePitch() - 5.0)
	def CameraSCD(self, argsList):
		if CyCamera().GetBasePitch() < 20:
			CyCamera().SetBasePitch(CyCamera().GetBasePitch() + 5.0)
	def CameraCH(self, argsList):
		CyCamera().SetBaseTurn(0)
		CyCamera().SetBasePitch(0)

### EVENT MANAGER ENTRY POINTS
	# Take multiple actions at the end of each player turn
	def onEndGameTurn(self, argsList):
		self.Initialize()
		iGameTurn = argsList[0]
		(iUnowned, iSpiceCount) = self.MapLoopRoutines() #!M!
		self.BlowAdd(iSpiceCount)
		self.WormAdd(iUnowned)
		self.StormRun()
		self.TerraVictoryCheck()
		self.SpiceVictoryCheck()
		objMercenaryUtils.doHomeworld() # koma13

        # Perform several steps when game loads (or starts, or python reloaded)
	def onGameLoad(self, argsList):
		self.Initialize()
		self.ContractStart()
		self.SpiceVictoryCheck()
		self.TerraVictoryCheck()
		# Create list of ocean plots
		self.lOcean = []
		for iPlotLoop in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotLoop)
			if pPlot.getTerrainType() == self.iTOcean:
				self.lOcean.append(pPlot)

	# Perform several steps when game starts
	def onGameStart(self, argsList):
		self.onGameLoad([])
		# Place initial spice
		xmax = CyMap().getGridWidth() ; ymax = CyMap().getGridHeight()
		iBlowWant = (xmax * ymax / 50)
		if iBlowWant > 0:
                        for i in xrange(iBlowWant):
                                for iTry in xrange(100):
                                        cx = CyGame().getSorenRandNum(xmax, "")
                                        cy = CyGame().getSorenRandNum(ymax, "")
                                        pPlot = CyMap().plot(cx, cy)
                                        if not pPlot.isWormFriendly(): continue
                                        if pPlot.isFreshWater(): continue
                                        self.SpiceAdd(cx, cy)
                                        break
										
										
		# Remove several terrains which may be added by mapscripts
		for iPlotLoop in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotLoop)
			iType = pPlot.getTerrainType()
			if iType == self.iTTGrass:
				pPlot.setTerrainType(self.iTRock, true, true)
			elif iType == self.iTTPlain:
				pPlot.setTerrainType(self.iTRug, true, true)
		# Initialize storm storage
		CyMap().plot(0,0).setScriptData("")

	def onBeginPlayerTurn(self, argsList):
		iGameTurn, iPlayer = argsList
		pPlayer = gc.getPlayer(iPlayer)	
		if pPlayer.hasTrait(self.iTraitABo):
			if CyGame().getSorenRandNum(100, "") < 3:
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_TRAIT_ABOMINATION')
				triggerData = pPlayer.initTriggeredData(iEvent, true, -1, -1, -1, iPlayer, -1, -1, -1, -1, -1)
		
	# Receive modnetmessage for various button presses
	def onModNetMessage(self, argsList):
		iMessageID, iData2, iData3, iData4, iData5 = argsList
		# Homeworld Screen: koma13
		if iMessageID == 690:
			pCity, pUnit = objMercenaryUtils.placeMercenaries(argsList)
                #!M! ->
                #Inquisition:
                elif iMessageID == 8586:
                        pUnit = gc.getPlayer(iData2).getUnit(iData3)
			if pUnit.movesLeft() > 0:
                                pCity = pUnit.plot().getPlotCity()
                                iPlayer = iData2; iReligion = iData4
                                ReligionInfo = gc.getReligionInfo(iReligion)
                                iMahdi = ReligionTypes.MAHDI
                                iMahdiPenalty = 0
                                
                                if gc.getPlayer(iPlayer).getStateReligion() == iMahdi:
                                        iMahdiPenalty = -30
                                elif iReligion == iMahdi:
                                        iMahdiPenalty = 30

                                bPurgeSucess = False
                                        
                                if (CyGame().getSorenRandNum(100, "") + iMahdiPenalty) < \
                                   (90 - CyGame().calculateReligionPercent(iReligion)):
                                        bPurgeSucess = True

                                if bPurgeSucess:
                                        pCity.setHasReligion(iReligion, False, True, True)
                                        
                                        CyInterface().addMessage(iPlayer, True, 15, CyTranslator().getText("TXT_PURGE_SUCCESS",(ReligionInfo.getDescription().capitalize(), pCity.getName(),)),'AS2D_PLAGUE',0,ReligionInfo.getButton(), gc.getInfoTypeForString("COLOR_POSITIVE_TEXT"), pCity.getX(), pCity.getY(), True,True)
                                        for iPlay in xrange(gc.getMAX_CIV_PLAYERS()):
                                                if iPlay == iPlayer: continue
                                                pPlay = gc.getPlayer(iPlay)
                                                if not pPlay.isAlive(): continue
                                                if pCity.isRevealed(pPlay.getTeam(), false):
                                                        CyInterface().addMessage(iPlay, false, 15, CyTranslator().getText("TXT_KEY_MESSAGE_INQUISITION_GLOBAL",(ReligionInfo.getDescription().capitalize(), pCity.getName(),)), "", 0, "", -1, -1, -1, false, false)
                                else:
                                        CyInterface().addMessage(iPlayer, True, 15, CyTranslator().getText("TXT_PURGE_FAILURE",(ReligionInfo.getDescription().capitalize(), pCity.getName(),)),'AS2D_SABOTAGE',0,ReligionInfo.getButton(), gc.getInfoTypeForString("COLOR_WARNING_TEXT"), pCity.getX(), pCity.getY(), True,True)
                                pUnit.kill(False, -1)
                ##Tleilaxu Gholas:
		elif iMessageID == 8999:
                        self.TleilaxuGhola(iData2, iData3, iData4)
                #Mentat
                elif iMessageID == 4455:
                        pUnit = gc.getPlayer(iData2).getUnit(iData3)
                        pCity = pUnit.plot().getPlotCity()
                        iBldg = iData4
                        
                        if pCity.getScriptData() != "":
                                iOldBldg = int(pCity.getScriptData())
                                if pCity.getNumRealBuilding(iOldBldg) > 0:
                                        pCity.setNumRealBuilding(iOldBldg, 0)
                                if pCity.getNumRealBuilding(iOldBldg + 1) > 0:
                                        pCity.setNumRealBuilding(iOldBldg + 1, 0)
                        if pCity.getNumBonuses(self.iBonusSapho) > 0:
                                pCity.setNumRealBuilding(iBldg + 1, 1)
                        else:
                                pCity.setNumRealBuilding(iBldg, 1)
                        pCity.setScriptData("%d" % iBldg)
                        
                        pUnit.getGroup().pushMission(MissionTypes.MISSION_FORTIFY, 0, 0, 0, false, false, MissionAITypes.NO_MISSIONAI, pUnit.plot(), pUnit)
			pUnit.finishMoves()
			
	# Check several conditions when city is built
	def onCityBuilt(self, argsList):
		pCity = argsList[0]
		self.Initialize()
		pPlay = gc.getPlayer(pCity.getOwner())
		iCiv = pPlay.getCivilizationType()
		# Add Tlei religion if Tlei city; found the religion when settling first city
		if iCiv == self.iCTlei:
			if not gc.getGame().isReligionFounded(self.iRTlei):
				pPlay.foundReligion(self.iRTlei, self.iRTlei, true)
			pCity.setHasReligion(self.iRTlei, true, false, false)
			if pPlay.getStateReligion() < 0:
                                pPlay.convert(self.iRTlei)
                #!M!
		elif pPlay.getStateReligion() == self.iRMahdi:
                        pCity.setHasReligion(self.iRMahdi, true, true, false)
		# If not capitol or Fremen, assign name from global list
		if (not pCity.isCapital()) and (iCiv != self.iCFrem):
			pCity.setName(self.MakeCityName(pCity), false)

	# Check several conditions when city changes hands
	def onCityAcquired(self, argsList):
		iPreviousOwner,iNewOwner,pCity,bConquest,bTrade = argsList
		self.Initialize()
		pNewOwner = gc.getPlayer(iNewOwner)
		# Add Tleilaxu religion if city now owned by Tlei
		if pNewOwner.getCivilizationType() == self.iCTlei:
			pCity.setHasReligion(self.iRTlei, true, false, false)
		# If conqueror state religion is Mahdi, spread it
		elif pNewOwner.getStateReligion() == self.iRMahdi:
			pCity.setHasReligion(self.iRMahdi, true, false, false)
		
	# Religion has spread to a city.  If Imperial is there remove it. ALN-leave holy city
	# If Qizarate is the one spreading, remove all others. ALN-leave holy cities
	def onReligionSpread(self, argsList):
                iReligion, iOwner, pCity = argsList
		if pCity.isHasReligion(self.iRImp) and iReligion != self.iRImp:
			if not pCity.isHolyCityByType(self.iRImp):
				pCity.setHasReligion(self.iRImp, false, false, false)
		if iReligion == self.iRQiz:
			for i in xrange(gc.getNumReligionInfos()):
				if i == self.iRQiz: continue
				if pCity.isHolyCityByType(i): continue
				if pCity.isHasReligion(i):
					pCity.setHasReligion(i, false, false, false)

### LOW LEVEL SUBROUTINES
	# Unsafe to perform getInfoTypeForString without checking success
	def GetCheckInfo(self, s):
		iVal = gc.getInfoTypeForString(s)
		if iVal == -1: self.DebugPrint ("GCI: Unable to find " + s)
		return iVal

	def Initialize(self):
		if self.bInitialized: return
		self.bInitialized = true
		self.DebugFilename = "c:\\stats.csv"

		self.iTraitABo = self.GetCheckInfo('TRAIT_ABOMINATION')
		self.iBonusSapho = self.GetCheckInfo("BONUS_SAPHO")
		self.iBSpice  = self.GetCheckInfo("BONUS_SPICE")
		self.iBWCSat  = self.GetCheckInfo("BUILDINGCLASS_WEATHER_CONTROL_SATELLITE")
		self.iBWine   = self.GetCheckInfo("BUILDING_CALADANIAN_WINE_CONTRACT")
		self.iBOpaf   = self.GetCheckInfo("BUILDING_OPAFIRE_CONTRACT")
		self.iBSlig   = self.GetCheckInfo("BUILDING_SLIG_CONTRACT")
		self.iBSardau = self.GetCheckInfo("BUILDING_SARDAUKAR_CONTRACT")
		self.iBIxWeap = self.GetCheckInfo("BUILDING_IX_WEAP_CONTRACT")
		self.iBKind   = self.GetCheckInfo("BUILDING_KINDJAL_CONTRACT")
		self.iBSapho  = self.GetCheckInfo("BUILDING_SAPHO_JUICE_CONTRACT")
		self.iBLabor  = self.GetCheckInfo("BUILDING_LABOR_CONTRACT")
		self.iBSoo    = self.GetCheckInfo("BUILDING_SOOSTONE_CONTRACT")
		self.iBPundi  = self.GetCheckInfo("BUILDING_PUNDI_RICE_CONTRACT")
		self.iBRichese = self.GetCheckInfo("BUILDING_RICHESE_CONTRACT")
		self.iBClassCatch  = self.GetCheckInfo("BUILDINGCLASS_CATCHBASIN")
		self.iBClassLiet   = self.GetCheckInfo("BUILDINGCLASS_RESERVOIR_OF_LIET")
		self.iBClassStage  = self.GetCheckInfo("BUILDINGCLASS_LANDING_STAGE")
		self.iBClassWine   = self.GetCheckInfo("BUILDINGCLASS_CALADANIAN_WINE_CONTRACT")
		self.iBClassSardau = self.GetCheckInfo("BUILDINGCLASS_SARDAUKAR_CONTRACT")
		self.iBClassIxWeap = self.GetCheckInfo("BUILDINGCLASS_IX_WEAP_CONTRACT")
		self.iBClassRichese = self.GetCheckInfo("BUILDINGCLASS_RICHESE_CONTRACT")
		self.iCArrak  = self.GetCheckInfo("CIVICOPTION_ARRAKIS")
		self.iCPara   = self.GetCheckInfo("CIVIC_ARRAKIS_PARADISE")
		self.iCSpind  = self.GetCheckInfo("CIVIC_ARRAKIS_SPICE")
		self.iCAtre   = self.GetCheckInfo("CIVILIZATION_ATREIDES")
		self.iCCorr   = self.GetCheckInfo("CIVILIZATION_CORRINO")
		self.iCFrem   = self.GetCheckInfo("CIVILIZATION_FREMEN")
		self.iCIx     = self.GetCheckInfo("CIVILIZATION_IX")
		self.iCTlei   = self.GetCheckInfo("CIVILIZATION_TLEILAX")
		self.iCRichese = self.GetCheckInfo("CIVILIZATION_RICHESE")
		self.iESandL  = self.GetCheckInfo("EFFECT_SANDSTORM_LIGHT")
		self.iESandD  = self.GetCheckInfo("EFFECT_SANDSTORM_DARK")
		self.iERain   = self.GetCheckInfo("EFFECT_RAINSTORM")
		self.iFBlow   = self.GetCheckInfo("FEATURE_SPICEBLOW")
		self.iFSpice  = self.GetCheckInfo("FEATURE_SPICE")
		self.iFForest = self.GetCheckInfo("FEATURE_FOREST")		
		self.iIHarv   = self.GetCheckInfo("IMPROVEMENT_HARVESTER")
		self.iRImp    = self.GetCheckInfo("RELIGION_IMPERIAL")
		self.iRMahdi  = self.GetCheckInfo("RELIGION_MAHDI")
		self.iRQiz    = self.GetCheckInfo("RELIGION_QIZARATE")
		self.iRTlei   = self.GetCheckInfo("RELIGION_TLEILAXU")
		self.iTGrab   = self.GetCheckInfo("TERRAIN_PLAINS")
		self.iTOcean  = self.GetCheckInfo("TERRAIN_OCEAN")
		self.iTCoast  = self.GetCheckInfo("TERRAIN_COAST")
		self.iTPolar  = self.GetCheckInfo("TERRAIN_POLAR")
		self.iTPSink  = self.GetCheckInfo("TERRAIN_POLAR_PLAINS")
		self.iTPCoast = self.GetCheckInfo("TERRAIN_POLAR_COAST")
		self.iTRock   = self.GetCheckInfo("TERRAIN_GRASS")
		self.iTRug    = self.GetCheckInfo("TERRAIN_SNOW")
		self.iTSalt   = self.GetCheckInfo("TERRAIN_SALT")
		self.iTTGrass = self.GetCheckInfo("TERRAIN_TERRA_GRASS")
		self.iTTPlain = self.GetCheckInfo("TERRAIN_TERRA_PLAINS")
		self.iTDunes  = self.GetCheckInfo("TERRAIN_DESERT")
		self.iTSpiceOcean = self.GetCheckInfo("TERRAIN_SPICE_OCEAN")
		self.iTSpiceCoast = self.GetCheckInfo("TERRAIN_SPICE_COAST")
		self.iUWorm1  = self.GetCheckInfo("UNIT_WORM1")
		self.iUWorm2  = self.GetCheckInfo("UNIT_WORM2")
		self.iUWorm3  = self.GetCheckInfo("UNIT_WORM3")
		self.iUWorm4  = self.GetCheckInfo("UNIT_WORM4")
		self.iUClassWorm = self.GetCheckInfo('UNITCLASS_WORM')
		self.iUCombatWorker = self.GetCheckInfo("UNITCOMBAT_WORKER")
		self.iUGhola = self.GetCheckInfo('UNIT_GHOLA')
		self.iVTerra = self.GetCheckInfo("VICTORY_TERRAFORMING")
		self.iVSpice = self.GetCheckInfo("VICTORY_SPICE")
		self.iUpdateTimer = 0
		self.iSpeedPct = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getImprovementPercent()
		self.iTargetCities = gc.getWorldInfo(gc.getMap().getWorldSize()).getTargetNumCities()
		self.iUTPGA = gc.getHandicapInfo(CyGame().getHandicapType()).getUnownedTilesPerGameAnimal()
		self.dContracts = {}
		self.dTerraformCount = {}
		self.dSpiceVictoryCount = {}

	# Print a debug message to file
	def DebugPrint(self, txt):
		f = open(self.DebugFilename, "a")
		f.write(txt + "\n")
		f.close()

	#!M! -> new Ghola:
	def TleilaxuGhola(self, iPlayer, iGholaID, iCellsID):
                SD_MOD_ID = "GeneticDataID: " + str(iPlayer)
                UNITS_DATA = "UnitsData" 
		GeneticData = BugData.getGameData().getTable(SD_MOD_ID)
                UnitsData = GeneticData[UNITS_DATA]
                pPlayer = gc.getPlayer(iPlayer)
		pHatchedTank = pPlayer.getUnit(iGholaID)
                id = iCellsID
                
                #Equipment/material cost
                pPlayer.changeGold(-gc.getUnitInfo(UnitsData[id]["UnitType"]).getProductionCost())
                        
                #Init proper ghola and store ID
		pGhola = pPlayer.initUnit(UnitsData[id]["UnitType"], pHatchedTank.getX(), pHatchedTank.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.NO_DIRECTION)
		pGhola.convert(pHatchedTank)
		
		UnitsData[id] = { "UnitType" : UnitsData[id]["UnitType"],
                                  "Exp" : UnitsData[id]["Exp"],
                                  "Level" : UnitsData[id]["Level"],
                                  "Promotions" : UnitsData[id]["Promotions"],
                                  "Name" : UnitsData[id]["Name"],
                                  "Death Date" : UnitsData[id]["Death Date"],
                                  "GholaID" : pGhola.getID() }
                GeneticData = { UNITS_DATA: UnitsData }
                BugData.getTable(SD_MOD_ID).setData(GeneticData)
                
		#Promos:
		iNumPromosLost = 0
		iStartingPromos = len(UnitsData[id]["Promotions"])
		for i in xrange(iStartingPromos):
			if CyGame().getSorenRandNum(100, "") < 33:
				iNumPromosLost += 1
		lValidPromos = []
		lPromosLost = []
		for i in xrange(gc.getNumPromotionInfos()):
                        if i in UnitsData[id]["Promotions"]:
                                if gc.getUnitInfo(UnitsData[id]["UnitType"]).getFreePromotions(i): continue
				lValidPromos.append(i)
		# put in a safety valve
		if iNumPromosLost > len(lValidPromos):
			iNumPromosLost = len(lValidPromos)
		for i in xrange(iNumPromosLost):
			lMayLose = []
			lPrereqs = []
			for i in lValidPromos:
				# check prereqs to detiremine which promos are currently at the top level
				iPrereqAND = gc.getPromotionInfo(i).getPrereqPromotion()
				iPrereqOr1 = gc.getPromotionInfo(i).getPrereqOrPromotion1()
				iPrereqOr2 = gc.getPromotionInfo(i).getPrereqOrPromotion2()
				if iPrereqAND == -1 and iPrereqOr1 == -1 and iPrereqOr2 == -1:
					continue
				for j in lValidPromos:
					bPrereq = false
					if j == i: continue
					if lPrereqs.count(j) > 0: continue
					if j == iPrereqAND: bPrereq = true
					# if only one OR prereq, it can't be taken away
					if iPrereqOr1 == -1 or iPrereqOr2 == -1:
						if j == iPrereqOr1: bPrereq = true
						if j == iPrereqOr2: bPrereq = true
					# if two OR prereqs AND the unit has both, either can be taken away
					# if the unit doesn't have the other, then we can't take it away
					else:
						if j == iPrereqOr1:
							for k in xrange(gc.getNumPromotionInfos()):
								if k == iPrereqOr2:
									if not pGhola.isHasPromotion(k):
										bPrereq = true
						if j == iPrereqOr2:
							for k in xrange(gc.getNumPromotionInfos()):
								if k == iPrereqOr1:
									if not pGhola.isHasPromotion(k):
										bPrereq = true
					if bPrereq == true:
						lPrereqs.append(j)
			for i in lValidPromos:
				if lPrereqs.count(i) == 0:
					lMayLose.append(i)
			if lMayLose != []:
				posn = CyGame().getSorenRandNum(len(lMayLose), "")
				lPromosLost.append(lMayLose[posn])
				lValidPromos.remove(lMayLose[posn])
		# Copy the promotions except the lost one/excluded ones
		iPromoCount = 0
		for i in xrange(gc.getNumPromotionInfos()):
			if lPromosLost.count(i) > 0: continue
			if i in UnitsData[id]["Promotions"]:
				pGhola.setHasPromotion(i, 1)
				iPromoCount += 1
		#Level:
		pGhola.changeLevel(iPromoCount)
		#Exp:
		iGeneticExp = (UnitsData[id]["Exp"] / 2)
		iRandGeneticExp = (CyGame().getSorenRandNum(iGeneticExp, "") + iGeneticExp)
		pGhola.setExperience(iRandGeneticExp, -1)
		#for Custom Names:
		szName = (UnitsData[id]["Name"] + " - Ghola")
		pGhola.setName(szName)
		#One more small slap in the butt and off to the big bad world:
		pGhola.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GHOLA'), True)
		pGhola.testPromotionReady()
                CyInterface().addMessage(iPlayer, True, 20, CyTranslator().getText("TXT_GHOLA_COMPLETED", (UnitsData[id]["Name"],)), 'AS2D_UNIT_BUILD_UNIT', 2, gc.getUnitInfo(pGhola.getUnitType()).getButton(), ColorTypes(12), pGhola.getX(), pGhola.getY(), True, True)

	# Make a city name with a terrain specific suffix (by deliverator)
	def MakeCityName(self, pCity):
		pBarb = gc.getPlayer(gc.getBARBARIAN_PLAYER())
		iBarbCiv = pBarb.getCivilizationType()
		pInfo = gc.getCivilizationInfo(iBarbCiv)
		n = pInfo.getNumCityNames()
		i = CyGame().getSorenRandNum(n, "")
		hillsSuffixArray = ["TXT_KEY_HILLS_SUFFIX_01", "TXT_KEY_HILLS_SUFFIX_02", "TXT_KEY_HILLS_SUFFIX_03", "TXT_KEY_HILLS_SUFFIX_04"]
		nonHillsSuffixArray = ["TXT_KEY_NONHILLS_SUFFIX_01", "TXT_KEY_NONHILLS_SUFFIX_02", "TXT_KEY_NONHILLS_SUFFIX_03", "TXT_KEY_NONHILLS_SUFFIX_04", "TXT_KEY_NONHILLS_SUFFIX_05"]
		exceptionsArray = ["TXT_KEY_EXCEPTION_SUFFIX_01", "TXT_KEY_EXCEPTION_SUFFIX_02", "TXT_KEY_EXCEPTION_SUFFIX_03"]
		baseCityName = pInfo.getCityNames(i)
		baseCityName = CyTranslator().getText(baseCityName, ("",))
		allSuffixArray = []
		allSuffixArray.extend(hillsSuffixArray)
		allSuffixArray.extend(nonHillsSuffixArray)
		allSuffixArray.extend(exceptionsArray)
		cityNameSuffix = ""
		bAppendTerrainSuffix = true
		for mySuffix in allSuffixArray:
			changedSuffix = CyTranslator().getText(mySuffix, ("",))
			if changedSuffix in baseCityName:
				bAppendTerrainSuffix = false
				break
		if bAppendTerrainSuffix == true:
			if pCity.plot().isHills():
				ihs = CyGame().getSorenRandNum(len(hillsSuffixArray) + 1, "")
				if ihs < len(hillsSuffixArray):
					cityNameSuffix = hillsSuffixArray[ihs]
					baseCityName = CyTranslator().getText(cityNameSuffix, (baseCityName,))
			else:
				ihs = CyGame().getSorenRandNum(len(nonHillsSuffixArray) + 1, "")
				if ihs < len(nonHillsSuffixArray):
					cityNameSuffix = nonHillsSuffixArray[ihs]
					baseCityName = CyTranslator().getText(cityNameSuffix, (baseCityName,))
		return baseCityName

### END OF TURN ROUTINES
	# Add new spice blows
	def BlowAdd(self, iSpiceCount):
		xmax = CyMap().getGridWidth() ; ymax = CyMap().getGridHeight()
		# Compute the number of blows to be added
		iBlowWant = (xmax * ymax / 50) - (iSpiceCount / 8)
		if iBlowWant > 0:
                        # Add the blows at random locations
                        for i in xrange(iBlowWant):
                                for iTry in xrange(100):
                                        cx = CyGame().getSorenRandNum(xmax, "")
                                        cy = CyGame().getSorenRandNum(ymax, "")
                                        pPlot = CyMap().plot(cx, cy)
                                        if not pPlot.isWormFriendly(): continue
                                        if pPlot.isFreshWater(): continue
                                        pPlot.setFeatureType(self.iFBlow, 0)
                                        break

	# Add spice bonuses in radius after a blow
	def SpiceAdd(self, cx, cy):
		xmax = CyMap().getGridWidth() ; ymax = CyMap().getGridHeight ()
		for ix in xrange(cx-1, cx+2):
			if (ix < 0) or (ix >= xmax): continue
			for iy in xrange(cy-1, cy+2):
				if (iy < 0) or (iy >= ymax): continue
				pPlot = CyMap().plot(ix, iy)
				if not pPlot.isWormFriendly(): continue
				if pPlot.isFreshWater(): continue
				iRnd = CyGame().getSorenRandNum(100, "")
				if iRnd < 77:
					pPlot.setBonusType(self.iBSpice)
					pPlot.setFeatureType(self.iFSpice, 0)
					iType = pPlot.getTerrainType()
					if iType == self.iTOcean:
						pPlot.setTerrainType(self.iTSpiceOcean, true, true)
					elif iType == self.iTCoast:
						pPlot.setTerrainType(self.iTSpiceCoast, true, true)

        # Count existing unowned valid for worms, ~spice
	# Randomly remove spice, faster if it has a harvester, slower if the owner follows the Spice Industry civic
	# Check all spiceblow features and give ~25% chance to convert to spice
	# Terraform upgrade/downgrade
	def MapLoopRoutines(self):
                dChances = self.ArrakisCivicsEffects()
                iSpiceCount = 0 ; iUnowned = 0
		for iPlotLoop in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotLoop)
			if pPlot.isWormFriendly():
                                #!M! -> Count unowned valid for worms
                                if not pPlot.isOwned():
                                        iUnowned += 1
                                #!M! -> Spice Decay routine
                                iType = pPlot.getBonusType(-1)
                                if iType == self.iBSpice:
                                        iSpiceCount += 1
                                        iImpr = pPlot.getImprovementType()
                                        bSpind = false
                                        iPlay = pPlot.getOwner()
                                        if iPlay != -1:
                                                pPlay = gc.getPlayer(iPlay)
                                                if pPlay.getCivics(self.iCArrak) == self.iCSpind:
                                                        bSpind = true
                                        if bSpind: 
                                                iChance = 50
                                        else:
                                                if iImpr == self.iIHarv:
                                                        iChance = 175
                                                else:
                                                        iChance = 55
                                        iChance = int (100 * iChance / self.iSpeedPct)
                                        if CyGame().getSorenRandNum(10000, "") < iChance:
                                                pPlot.setFeatureType(-1, 0)
                                                pPlot.setBonusType(-1)
                                                iType = pPlot.getTerrainType()				
                                                if iType == self.iTSpiceOcean:
                                                        pPlot.setTerrainType(self.iTOcean, true, true)
                                                elif iType == self.iTSpiceCoast:
                                                        pPlot.setTerrainType(self.iTCoast, true, true)
                                                if iImpr == self.iIHarv:
                                                        pPlot.setImprovementType(-1)
                                #!M! -> Spice Blow routine
                                if pPlot.getFeatureType() == self.iFBlow:
                                        iSpiceCount += 8
                                        if CyGame().getSorenRandNum(1000, "") < 250:
                                                pPlot.setFeatureType(-1, 0)
                                                self.SpiceAdd(pPlot.getX(), pPlot.getY())
                        #!M! -> Terraform routine
                        elif not pPlot.isPeak():
                                bUp = false
                                iPlay = pPlot.getOwner()
                                if dChances.has_key(iPlay) and pPlot.isFreshWater():
                                        pPlay = gc.getPlayer(iPlay)
                                        if pPlay.getCivics(self.iCArrak) == self.iCPara:
                                                bUp = true
                                if bUp:
                                        self.TerraformUp(pPlot, dChances)
                                else:
                                        if pPlot.getFeatureType() == self.iFForest:
                                                pPlot.setFeatureType(-1, 0)
                                        iChance = 15 * 100 / self.iSpeedPct
                                        if CyGame().getSorenRandNum(100, "") < iChance:
                                                self.TerraformDown(pPlot)
                                        
                return (iUnowned,iSpiceCount)
                                
### TERRAFORMING ROUTINES
	# Terraforming for cities. Count reservoirs for diplo penalty, and
	# remove catch/reservoir if nonmatching civic.  Return chance of
	# terraform upgrade for each player, based on number of reservoirs.
	def ArrakisCivicsEffects(self):
		lIndustry = [] ; lNeutral = [] ; dChances = {}
		# List players with and without spice industry civic
		for iPlay in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlay = gc.getPlayer(iPlay)
			if not pPlay.isAlive(): continue
			if pPlay.isHuman(): continue
			if pPlay.getCivics(self.iCArrak) == self.iCSpind:
				lIndustry.append(pPlay)
			else:
				lNeutral.append(pPlay)
		for iPlay in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlay = gc.getPlayer(iPlay)
			if not pPlay.isAlive(): continue
			# Set reaction count of industry players to -2*rescount
			iResCount = pPlay.getBuildingClassCount(self.iBClassLiet)
			if len(lIndustry) > 0:
				iPen = -2 * iResCount
				if iPen < -8: iPen = -8
				for pPlay2 in lIndustry:
					pPlay2.AI_setAttitudeExtra(iPlay, iPen)
			if len(lNeutral) > 0:
				for pPlay2 in lNeutral:
					pPlay2.AI_setAttitudeExtra(iPlay, 0)
			# Set chance of terraform upgrade
			bHasParadise = false
			if pPlay.getCivics(self.iCArrak) == self.iCPara:
				bHasParadise = true
			if bHasParadise:
                                iCatchCount = pPlay.getBuildingClassCount(self.iBClassCatch)
                                iCities = pPlay.getNumCities()
				# ALN - put in some breaks on the system - lots of cities come at a cost
				iCities = max(0, iCities - self.iTargetCities)
				dChances[iPlay] = 10 + max(0, (2 * iCatchCount) + (5 * iResCount) - (2 * iCities))
		return dChances	
		
	# This plot does not qualify for terraforming.  If terraformed high chance to undo back to base terrain.
	# Grass to plains.  In sinks, plains to graben, else plains to rock.
	def TerraformDown(self, pPlot):
		iType = pPlot.getTerrainType()
		iX = pPlot.getX()
		iY = pPlot.getY()
		bPolar = false
		for eDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
			pAdjacentPlot = plotDirection(iX, iY, DirectionTypes(eDirection))
			if not pAdjacentPlot.isNone():
				iAdjacentType = pAdjacentPlot.getTerrainType()
				if (iAdjacentType == self.iTPolar or iAdjacentType == self.iTPSink):
					bPolar = true
					break		
		if not bPolar:
			if iType == self.iTTGrass:
				iNew = self.iTTPlain
			elif iType == self.iTTPlain:
				if pPlot.isHills(): 
					iNew = self.iTGrab
				else: 
					iNew = self.iTRock
			else:
                                return
		else:
			if iType == self.iTTGrass:
				if pPlot.isHills():
					iNew = self.iTPSink
				else:
					iNew = self.iTPolar
			else:
				return
		pPlot.setTerrainType(iNew, true, true)
		return

	# This plot qualifies for terraforming.  Salt to graben to plains;
	# badland or rugged to rock; rock to plains; plains to grass.
	def TerraformUp(self, pPlot, dChances):
		iChance = dChances[pPlot.getOwner()]
		iChance = int (100.0 * iChance / self.iSpeedPct)
		# ALN - Base the chances of terraforming on world size to compensate for more or less cities
		# was 1000 for all before, still 1000 for standard size world (5 target cities)
		iTotalOdds = self.iTargetCities * 200
		iType = pPlot.getTerrainType()
		if iType == self.iTSalt: iNew = self.iTGrab
		elif iType == self.iTGrab: iNew = self.iTTPlain
		elif iType == self.iTRug:
			iNew = self.iTRock
			iChance = iChance / 2
		elif iType == self.iTRock: iNew = self.iTTPlain
		elif iType == self.iTTPlain: iNew = self.iTTGrass
		elif iType == self.iTPolar:
			iNew = self.iTTGrass
			iChance /= 3
		elif iType == self.iTPSink:
			iNew = self.iTTGrass
			iChance /= 5
		elif iType == self.iTTGrass:
			# Possible forest
			if pPlot.getFeatureType() != -1: return
			if pPlot.getBonusType(TeamTypes.NO_TEAM) != -1: return
			if not pPlot.isHills(): return
			if CyGame().getSorenRandNum(iTotalOdds, "") < (iChance * 2 / 3):
				pPlot.setFeatureType(self.iFForest, 0)		
			return
		else: return
		if CyGame().getSorenRandNum(iTotalOdds, "") >= iChance: return
		pPlot.setTerrainType(iNew, true, true)

### WORM ROUTINES
	def WormAdd(self, iUnowned):
		xmax = CyMap().getGridWidth() ; ymax = CyMap().getGridHeight ()
		pBarb = gc.getPlayer(gc.getBARBARIAN_PLAYER())
		iWormCount = pBarb.getUnitClassCount(self.iUClassWorm)
		# ALN - modify max number by game speed (using only half the normal adjustment)
		iMaxWorms = (iUnowned / (3 * self.iUTPGA)) * 100 / (100 + ((self.iSpeedPct - 100) / 2))
		iWormWant = iMaxWorms - iWormCount
		if iWormWant > 0:
                        # Compute the strength of the worm to be added
                        iEra = CyGame().getCurrentEra()
                        if iEra == 0 or iEra == 1: iWormUnit = self.iUWorm1
                        elif iEra == 2 or iEra == 3: iWormUnit = self.iUWorm2
                        elif iEra == 4 or iEra == 5: iWormUnit = self.iUWorm3
                        elif iEra == 6: iWormUnit = self.iUWorm4
                        # Add the worms at random locations
                        for i in xrange(iWormWant):
                                for iTry in xrange(100):
                                        pPlot = self.lOcean[CyGame().getSorenRandNum(len(self.lOcean), "")]
                                        if pPlot.isOwned(): continue
                                        pBarb.initUnit(iWormUnit, pPlot.getX(), pPlot.getY(),
                                                UnitAITypes.NO_UNITAI,
                                                DirectionTypes.DIRECTION_EAST)
                                        break

### STORM ROUTINES
	# Parse scriptdata of 0,0: convert x1,y1,t;x2,y2,t; ... into list of triples
	def StormList(self):
		lStorms = []
		s = CyMap().plot(0,0).getScriptData()
		if s != "":
			for lxyt in s.split(";"):
				(ix, iy, type) = lxyt.split(",")
				lStorms.append([int(ix),int(iy), int(type)])
		return lStorms

	# Draw storm effects, called by CvMainInterface::redraw
	def StormDraw(self):
		self.Initialize()
		self.iUpdateTimer += 1
		if self.iUpdateTimer == 12:
			self.iUpdateTimer = 0
			for lxyt in self.StormList():
				(ix, iy, iType) = lxyt
				pPoint = CyMap().plot(ix, iy).getPoint()
				if iType == 1:
					pPlot = CyMap().plot(ix, iy)
					iPlotType = pPlot.getTerrainType()
					if CyMap().plot(ix, iy).isWater() or iPlotType == self.iTDunes: iEffect = self.iESandD
					else: iEffect = self.iESandL
				else: iEffect = self.iESand # should be rain
				CyEngine().triggerEffect(iEffect, pPoint)

	# Top level storm routine: add/subtract, die, do damage, and move
	def StormRun(self):
		lOldStorms = self.StormAddSubtract()
		sNewStorms = ""
		for lxyt in lOldStorms:
			(ix, iy, type) = lxyt
			CyMap().plot(ix, iy).setSandstorm(false)			
			if not self.StormDie(ix, iy):
				(nx, ny) = self.StormMove(ix, iy)
				if nx != -1:
					sNewStorms += (";%d,%d,1" % (nx, ny))
					pPlot = CyMap().plot(nx, ny)
					pPlot.setSandstorm(true)
					if not pPlot.isCity():
                                                self.StormDamage(pPlot, nx, ny)
		CyMap().plot(0,0).setScriptData(sNewStorms[1:])

	# !M! ->
	def StormDamage(self, pPlot, iX, iY):
                iPlotImprov = pPlot.getImprovementType()
		if iPlotImprov > -1:
                        iChance = 50
                        if pPlot.isHills(): iChance = 10
                        elif pPlot.isPeak(): iChance = 2
                        elif pPlot.getTerrainType() == self.iTOcean: iChance = 90
                        iPlay = pPlot.getOwner()
                        if iPlay > -1 and not gc.getPlayer(iPlay).isHuman():
                                iChance /= 2
                                
                        if CyGame().getSorenRandNum(100, "") < iChance:
                                pPlot.setImprovementType(gc.getImprovementInfo(iPlotImprov).getImprovementPillage())
                                if iPlay > -1:
                                        CyInterface().addMessage(iPlay, True, 10, CyTranslator().getText("TXT_KEY_IMPROVEMENT_DESTROYED_ST", (gc.getImprovementInfo(iPlotImprov).getDescription(),)), "AS2D_COMBAT", 3, gc.getImprovementInfo(iPlotImprov).getButton(), ColorTypes(7), iX, iY, True, True)
                                        # !M! -> Show sandstorm image when applicable
                                        if gc.getPlayer(iPlay).isHuman() and not CyUserProfile().getGraphicOption(GraphicOptionTypes.GRAPHICOPTION_NO_MOVIES):
                                                if CyGame().isFinalInitialized():
                                                        if (not CyGame().isGameMultiPlayer()) and (iPlay == CyGame().getActivePlayer()):
                                                                popupInfo = CyPopupInfo()
                                                                popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
                                                                popupInfo.setData1(iPlotImprov) # iType
                                                                popupInfo.setData2(1) # iEventId
                                                                popupInfo.setText(u"showMiscScreens")
                                                                popupInfo.addPopup(iPlay)
                iPlotNumUnits = pPlot.getNumUnits()
                if iPlotNumUnits > 0:
                        iRandDamage = 10
			if pPlot.isPeak(): iRandDamage = 0
			elif pPlot.isWormFriendly(): iRandDamage = 25
			bShowImage = True
			
			for iUnit in xrange(iPlotNumUnits):
                                pUnit = pPlot.getUnit(iUnit)
                                if pUnit.isNone() or pUnit.getUnitClassType() == self.iUClassWorm: continue
                                
                                if pUnit.baseCombatStr() > 0:
                                        pUnit.changeDamage(15 + CyGame().getSorenRandNum(iRandDamage, ""), -1)
                                        if pUnit.isDead():
                                                CyInterface().addMessage(pUnit.getOwner(), True, 10, CyTranslator().getText("TXT_KEY_UNIT_DESTROYED_ST", (pUnit.getName(),)), "AS2D_COMBAT", 3, pUnit.getButton(), ColorTypes(7), iX, iY, True, True)
                                        else:
                                                CyInterface().addMessage(pUnit.getOwner(), True, 10, CyTranslator().getText("TXT_KEY_UNIT_DAMAGED_ST", (pUnit.getName(),)), "AS2D_COMBAT", 3, pUnit.getButton(), ColorTypes(11), iX, iY, True, True)
                                else:
                                        if pUnit.getUnitCombatType() == self.iUCombatWorker and CyGame().getSorenRandNum(100, "") < 8:
                                                CyInterface().addMessage(pUnit.getOwner(), True, 10, CyTranslator().getText("TXT_KEY_UNIT_DESTROYED_ST", (pUnit.getName(),)), "AS2D_COMBAT", 3, pUnit.getButton(), ColorTypes(7), iX, iY, True, True)
                                                pUnit.kill(true, -1)
                                        else:
                                                CyInterface().addMessage(pUnit.getOwner(), True, 10, CyTranslator().getText("TXT_KEY_UNIT_IMMOBILE_ST", (pUnit.getName(),)), "AS2D_COMBAT", 3, pUnit.getButton(), ColorTypes(11), iX, iY, True, True)
                                                pUnit.setImmobileTimer(2) #GameTurn has not ended yet (= 1)
                                # !M! -> Show sandstorm image when applicable (once per plot)
                                if gc.getPlayer(pUnit.getOwner()).isHuman() and bShowImage and not CyUserProfile().getGraphicOption(GraphicOptionTypes.GRAPHICOPTION_NO_MOVIES):
                                        if CyGame().isFinalInitialized():
                                                if (not CyGame().isGameMultiPlayer()) and (pUnit.getOwner() == CyGame().getActivePlayer()):
                                                        popupInfo = CyPopupInfo()
                                                        popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
                                                        popupInfo.setData1(-1) # iType
                                                        popupInfo.setData2(3) # iEventId
                                                        popupInfo.setText(u"showMiscMovieScreens")
                                                        popupInfo.addPopup(pUnit.getOwner())
                                                        bShowImage = False
                                                
	# Add new storms, then delete any which are adjacent
	def StormAddSubtract(self):
		lStorms = self.StormList()
		# Compute the number of storms to be added
		iMaxStorms = (len(self.lOcean) / 25) * 100 / (100 + ((self.iSpeedPct - 100) / 2))
		iStormWant = iMaxStorms - len(lStorms)
		if iStormWant > 0:
		# Add the storms at random locations
                        for i in xrange(iStormWant):
                                for iTry in xrange(100):
                                        pPlot = self.lOcean[CyGame().getSorenRandNum(len(self.lOcean), "")]
                                        if pPlot.isOwned(): continue
                                        lStorms.append([pPlot.getX(), pPlot.getY(), 1])
                                        break
		# Loop the list and delete one of an adjacent pair
		if CyGame().getCurrentEra() < 5:
                        n = len(lStorms)
                        lDeletes = []
                        for i in xrange(n-1):
                                (ix, iy, type) = lStorms[i]
                                for j in xrange(i+1, n):
                                        (jx, jy, type) = lStorms[j]
                                        if abs (ix - jx) > 2: continue
                                        if abs (iy - jy) > 2: continue
                                        # Tag the i position for deletion and skip to next i
                                        lDeletes.append(i)
                                        CyMap().plot(ix, iy).setSandstorm(false)	
                                        break
                        # To keep indices valid, reverse list (now largest to smallest)
                        if lDeletes != []:
                                lDeletes.reverse()
                                for i in lDeletes: del lStorms[i]
		return lStorms
	
	# Possibly kill storm on hill or peak, or due to weather satellite
	def StormDie(self, cx, cy):
		pPlot = CyMap().plot(cx, cy)
		iPlay = pPlot.getOwner()
		if (iPlay != -1) and (gc.getPlayer(iPlay).getBuildingClassCount(self.iBWCSat) > 0):
			return true
		iType = pPlot.getTerrainType()
		iRnd = CyGame().getSorenRandNum(100, "")
		if pPlot.isHills():
			if iRnd < 80: return true
		elif pPlot.isPeak(): return true
		elif iType == self.iTPCoast: return true
		elif iType == self.iTOcean: return false
		elif iRnd < 10: return true
		return false

	# Move one square east, possibly N/S; wrap, but die at pole
	def StormMove(self, cx, cy):
		xmax = CyMap().getGridWidth() ; ymax = CyMap().getGridHeight ()
		xchange = 0
		ychange = 0
		probxzero = 0
		probyzero = 0
		if cx < (xmax / 2):
			if cy < (ymax / 2):
				xchange = 1
				ychange = -1
				probxzero = 15
				probyzero = 35
			else:
				xchange = -1
				ychange = -1
				probxzero = 35
				probyzero = 15
		else:
			if cy < (ymax / 2):
				xchange = 1
				ychange = 1
				probxzero = 35
				probyzero = 15
			else:
				xchange = -1
				ychange = 1
				probxzero = 15
				probyzero = 35
		iRnd = CyGame().getSorenRandNum(100, "")
		if iRnd < probxzero:
			xchange = 0
		elif iRnd < (probxzero + probyzero):
			ychange = 0
		cx = cx + xchange
		cy = cy + ychange
		if cx == xmax or cx == -1 or cy == ymax or cy == -1: return (-1, -1)
		return (cx, cy)

### TRADE CONTRACTS
	# At game start, setup the array of acceptable contracts.  If the
	# owning civ is in the game, mark the player number.  If any civ may
	# build it, mark -1.  If it is already built, mark -2.
	def ContractStart(self):
		self.dContracts = {
			self.iBWine : -1, self.iBIxWeap : -1, self.iBSardau : -1,
			self.iBOpaf : -1, self.iBKind : -1, self.iBRichese : -1,
			self.iBSlig : -1, self.iBSoo : -1, self.iBPundi : -1,
			self.iBLabor : -1, self.iBSapho : -1
		}
		for iPlay in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlay = gc.getPlayer(iPlay)
			if not pPlay.isAlive(): continue
			iCiv = gc.getPlayer(iPlay).getCivilizationType()
			# !M!- > Only this civ may have this bonus
			# Don't forget to update SevoPediaBonus.py help
			if iCiv == self.iCCorr:
				self.dContracts[self.iBSardau] = iCiv
			elif iCiv == self.iCIx:
				self.dContracts[self.iBIxWeap] = iCiv
			elif iCiv == self.iCAtre:
				self.dContracts[self.iBWine] = iCiv
			elif iCiv == self.iCRichese:
                                self.dContracts[self.iBRichese] = iCiv
		# Set value to -2 if building exists anywhere
		lKeys = self.dContracts.keys()
		for iPlay in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlay = gc.getPlayer(iPlay)
			if not pPlay.isAlive(): continue
			(pCity, iter) = pPlay.firstCity(false)
			while (pCity):
                                for iKey in lKeys:
                                        if pCity.getNumRealBuilding(iKey) > 0 and self.dContracts[iKey] == -1:
                                                self.dContracts[iKey] = -2
				(pCity, iter) = pPlay.nextCity(iter, false)

	# Can this player build this contract?  Check if contract array is
	# -1 (anybody can build) or matching civ number.
	def ContractCan(self, argsList, sType):
		self.Initialize()
		if self.dContracts == {}: self.ContractStart()
		oTrigger = argsList[1]
		iPlayer = oTrigger.ePlayer
		pPlayer = gc.getPlayer(iPlayer)
		iKey = self.GetCheckInfo("BUILDING_" + sType + "_CONTRACT")
		if not self.dContracts.has_key(iKey): return false
		# Force civs to have to build their unique resource contract on second landing stage if not already built
		iCiv = pPlayer.getCivilizationType()
		if iCiv == self.iCAtre:
                        if pPlayer.getBuildingClassCount(self.iBClassStage) > 1 \
                           and pPlayer.getBuildingClassCount(self.iBClassWine) == 0 and not iKey == self.iBWine:
				return false
		elif iCiv == self.iCIx:
                        if pPlayer.getBuildingClassCount(self.iBClassStage) > 1 \
                           and pPlayer.getBuildingClassCount(self.iBClassIxWeap) == 0 and not iKey == self.iBIxWeap:
				return false
		elif iCiv == self.iCCorr:
                        if pPlayer.getBuildingClassCount(self.iBClassStage) > 1 \
                           and pPlayer.getBuildingClassCount(self.iBClassSardau) == 0 and not iKey == self.iBSardau:
				return false
		elif iCiv == self.iCRichese:
                        if pPlayer.getBuildingClassCount(self.iBClassStage) > 1 \
                           and pPlayer.getBuildingClassCount(self.iBClassRichese) == 0 and not iKey == self.iBRichese:
				return false

		if self.dContracts[iKey] == -1: return true
		iKeyClass = self.GetCheckInfo("BUILDINGCLASS_" + sType + "_CONTRACT")
		if self.dContracts[iKey] == iCiv and pPlayer.getBuildingClassCount(iKeyClass) < 1: return true
		return false
		
	# This player has built this contract; mark it built.
	def ContractDo(self, argsList, sType):
		self.Initialize()
		if self.dContracts == {}: self.ContractStart()
		iKey = self.GetCheckInfo("BUILDING_" + sType + "_CONTRACT")
		if not self.dContracts.has_key(iKey): return false
		if self.dContracts[iKey] == -1:
			self.dContracts[iKey] = -2

	# Help string for this contract
	def ContractHelp(self, argsList, sType):
		self.Initialize()
		if self.dContracts == {}: self.ContractStart()
		iPlay = gc.getActivePlayer().getID()
		iCiv = gc.getPlayer(iPlay).getCivilizationType()
		iKey = self.GetCheckInfo("BUILDING_" + sType + "_CONTRACT")
		s = gc.getBuildingInfo(iKey).getHelp()
		t = CyTranslator().getText("[ICON_BULLET]", ())
		if iKey == self.iBSlig:
			st2 = CyTranslator().getText("TXT_KEY_SLIG_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
		elif iKey == self.iBWine:
			st2 = CyTranslator().getText("TXT_KEY_CALWINE_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
		elif (iKey == self.iBOpaf) or (iKey == self.iBSoo):
			st2 = CyTranslator().getText("TXT_KEY_OPAFIRE_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
		elif iKey == self.iBPundi:
			st2 = CyTranslator().getText("TXT_KEY_PUNDI_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
		elif iKey == self.iBKind:
			st2 = CyTranslator().getText("TXT_KEY_GINAZ_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
		elif iKey == self.iBSardau:
			st2 = CyTranslator().getText("TXT_KEY_SARDAUKAR_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
			if iCiv == self.iCCorr:
				st2 = CyTranslator().getText("TXT_KEY_CORRINO_CONTRACT_STRATEGY", ())		
				s = t + st2 + "\n" + s
		elif iKey == self.iBIxWeap:
			st2 = CyTranslator().getText("TXT_KEY_IX_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
			if iCiv == self.iCIx:
				st2 = CyTranslator().getText("TXT_KEY_IXRECOM_CONTRACT_STRATEGY", ())		
				s = t + st2 + "\n" + s
		elif iKey == self.iBLabor:
			st2 = CyTranslator().getText("TXT_KEY_LABOR_CONTRACT_STRATEGY", ())
			s = t + st2 + "\n" + s
		elif iKey == self.iBRichese:
			st2 = CyTranslator().getText("TXT_KEY_BUILDING_RICHESE_STRATEGY", ())
			s = t + st2 + "\n" + s
		return s

### MENTAT FUNCTIONS
	# Event action function for mentat specialty
	def MentatDo(self, argsList, sType):
		iEvent = argsList[0]
		pData = argsList[1]
		self.Initialize()
		pPlay = gc.getPlayer(pData.ePlayer)
		pUnit = pPlay.getUnit(pData.iUnitId)
		iPromo = self.GetCheckInfo("PROMOTION_MENTAT_" + sType)
		pUnit.setHasPromotion(iPromo, 1)
		sBldg = gc.getPromotionInfo(iPromo).getType()
		sBldg = sBldg.replace("PROMOTION_", "BUILDING_")
		iBldg = gc.getInfoTypeForString(sBldg)
		pUnit.setScriptData("%d" % iBldg)

	# Event help function for mentat specialty
	def MentatHelp(self, argsList, sType):
		self.Initialize()
		sPromo = "PROMOTION_MENTAT_" + sType
		iPromo = self.GetCheckInfo(sPromo)
		return gc.getPromotionInfo(iPromo).getHelp()
                
### TERRAFORMING VICTORY FUNCTIONS
	def TerraVictoryPlots(self):
		self.Initialize()
		xmax = CyMap().getGridWidth()
		ymax = CyMap().getGridHeight()
		return int (xmax * ymax / 33)

	def TerraVictoryPlayer(self, iTeam):
		self.Initialize()
		if not self.dTerraformCount.has_key(iTeam): return 0
		return self.dTerraformCount[iTeam]

	def TerraVictoryCheck(self):
		self.Initialize()
		if not CyGame().isVictoryValid(self.iVTerra): return
		for iTeam in xrange(gc.getMAX_CIV_TEAMS()):
                        pTeam = gc.getTeam(iTeam)
                        if not pTeam.isAlive(): continue
			self.dTerraformCount[iTeam] = 0
		for iPlotLoop in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotLoop)
			if pPlot.getTerrainType() != self.iTTGrass: continue
			if pPlot.isBarbarian(): continue
			iTeam = pPlot.getTeam()
			if iTeam > -1: self.dTerraformCount[iTeam] += 1
		iWinThreshold = self.TerraVictoryPlots()
		for iTeam in xrange(gc.getMAX_CIV_TEAMS()):
                        pTeam = gc.getTeam(iTeam)
                        if not pTeam.isAlive(): continue
			iCount = self.dTerraformCount[iTeam]
			if iCount >= iWinThreshold:
				CyGame().setWinner(iTeam, 5)
			
### SPICE VICTORY FUNCTIONS
	def TotalSpiceOnArrakis(self):
		iCount = 0
		for iPlay in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlay = gc.getPlayer(iPlay)
			if not pPlay.isAlive(): continue
                        pCapital = pPlay.getCapitalCity()
                        if pCapital.getNumBonuses(self.iBSpice) > 0:
                                iCount += pCapital.getNumBonuses(self.iBSpice)
		return int (iCount)
	
	def SpiceVictoryRequiredBonuses(self):
		iCount = self.TotalSpiceOnArrakis()
		iPercentage = self.SpiceVictoryGetPercentage()
		return int (iCount * iPercentage / 100)
		
	def SpiceVictoryGetPercentage(self):
                if CyMap().getWorldSize() == 6:
                        iPercentageSpice = 45
                elif CyMap().getWorldSize() == 5:
                        iPercentageSpice = 50
                elif CyMap().getWorldSize() == 4:
                        iPercentageSpice = 55
                elif CyMap().getWorldSize() == 3:
                        iPercentageSpice = 60
                elif CyMap().getWorldSize() == 2:
                        iPercentageSpice = 65
                elif CyMap().getWorldSize() == 1:
                        iPercentageSpice = 70
                elif CyMap().getWorldSize() == 0:
                        iPercentageSpice = 75
		return iPercentageSpice

	def SpiceVictoryFixedAmount(self):
		self.Initialize()
		xmax = CyMap().getGridWidth()
		ymax = CyMap().getGridHeight()
		return int (xmax * ymax / 100)
		
	def SpiceVictoryPlayer(self, iTeam):
		self.Initialize()
		if not self.dSpiceVictoryCount.has_key(iTeam): return 0
		return self.dSpiceVictoryCount[iTeam]

	def SpiceVictoryCheck(self):
		self.Initialize()
		if not CyGame().isVictoryValid(self.iVSpice): return
		iWinFixedAmount = self.SpiceVictoryFixedAmount()
		iWinThreshold = self.SpiceVictoryRequiredBonuses()
		for iTeam in xrange(gc.getMAX_CIV_TEAMS()):
                        pTeam = gc.getTeam(iTeam)
                        if (not pTeam.isAlive()) or pTeam.isAVassal(): continue
                        iSpice = 0
                        for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
                                pCheckPlayer = gc.getPlayer(iPlayer)
                                if not pCheckPlayer.isAlive(): continue
                                iCheckTeam = pCheckPlayer.getTeam()
                                if not (iCheckTeam == iTeam or gc.getTeam(iCheckTeam).isVassal(iTeam)): continue
                                iSpice += pCheckPlayer.getCapitalCity().getNumBonuses(self.iBSpice)
                        self.dSpiceVictoryCount[iTeam] = iSpice
                        if iSpice >= iWinFixedAmount:
                                if iSpice >= iWinThreshold:
                                        CyGame().setWinner(iTeam, 6)
