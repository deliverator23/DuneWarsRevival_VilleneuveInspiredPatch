## Sid Meier's Civilization 4
## Copyright Firaxis Games 2008

from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums
import MercenaryUtils
import time
import BugData

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()
objMercenaryUtils = MercenaryUtils.MercenaryUtils()
SD_MOD_ID = "MercenaryData"
AVAILABLE_MERCENARIES = "AvailableMercenaries"
UNIQUE_ID = "UniqueID"
SEQUENCE = "Sequence"

class CvHomeworldAdvisor:
	"Homeworld Advisor Screen"

	def __init__(self):

		self.SCREEN_NAME = "HomeworldAdvisor"
				
		self.XResolution = 0
		self.YResolution = 0

		self.UNIT_LIST = 1
		self.CITY_LIST = 2
		self.LAUNCH_BUTTON = 3
		self.SEQUENCE_BUTTON = 4
		self.UNIT_INFO = 5
		self.CREDITS_BUTTON = 667
		
		self.isFremen = 0
		
	def interfaceScreen (self):

		self.player = gc.getPlayer(gc.getGame().getActivePlayer())
		if (not BugData.getGameData().getTable(SD_MOD_ID).hasTable(AVAILABLE_MERCENARIES)):
			objMercenaryUtils.setupMercenaryData()
			
		screen = self.getScreen()
		if screen.isActive():
			return
		
		self.UnitList = [] 		
		self.iSelectedCity = -1
		self.iTotalCost = 0
		self.iCurrentGold = self.player.getGold()
				
		self.XResolution = self.getScreen().getXResolution()
		self.YResolution = self.getScreen().getYResolution()

		self.isFremen = (self.player.getCivilizationType() == gc.getInfoTypeForString("CIVILIZATION_FREMEN"))
		
		screen.setRenderInterfaceOnly(False);
		screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)
		screen.setDimensions(0, 0, self.XResolution, self.YResolution)
		screen.showWindowBackground(False)
		
		CyInterface().setShowInterface(InterfaceVisibility.INTERFACE_MINIMAP_ONLY)
		CyInterface().clearSelectionList()
		
		self.fZoom = CyCamera().GetZoom()
		iW = CyMap().getGridWidth()
				
		fNewZoom = 0.6 - ((iW - 44.0) / 400.0)
		
		if CyMap().getGridWidth() == CyMap().getGridHeight():
			fNewZoom = 0.6 - ((iW - 32.0) / 200.0)
		
		if fNewZoom > 0.57:
			fNewZoom = 0.57
			
		CyCamera().SetZoom(fNewZoom)
		
		self.iCounter = 0
		self.bPlayTransition = false
		self.fTimeBackup = 0.0
		
		screen.addModelGraphicGFC("starsR", "Art/Interface/Screens/HomeWorld/AmphibiousBG.nif", self.XResolution / 2, 0, self.XResolution / 2, self.YResolution * 25 / 103, WidgetTypes.WIDGET_GENERAL, -1, -1, 0, 0, 1.0)
		screen.addDDSGFC("arrakisBackground", "Art/Interface/Screens/HomeWorld/heighliner3.dds", self.XResolution / 2, 0, self.XResolution / 2, self.YResolution * 2 / 3, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.addDDSGFC("blackBackground", "Art/Interface/Screens/HomeWorld/black.dds", 0, 0, self.XResolution / 2, self.YResolution, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.addUnitGraphicGFC("homeworld", gc.getInfoTypeForString("UNIT_HOMEWORLD"), 0, 0, self.XResolution / 2, self.YResolution * 13 / 12, WidgetTypes.WIDGET_GENERAL, -1, -1, 0, 0, 0.24, false)
		screen.addDDSGFC("homeworldLayer", "", 0, 0, self.XResolution / 2, self.YResolution, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		if not self.isFremen:
			for i in range(15):
				screen.addDDSGFC("blackScreenL" + str(i), "Art/Interface/Screens/HomeWorld/shaded.dds", 0, 0, self.XResolution / 2, self.YResolution, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				screen.hide("blackScreenL" + str(i))
			
			for i in range(15):
				screen.addDDSGFC("blackScreenR" + str(i), "Art/Interface/Screens/HomeWorld/shaded.dds", self.XResolution / 2, 0, self.XResolution / 2, self.YResolution, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				screen.hide("blackScreenR" + str(i))
			
			for i in range(9):
				screen.addDDSGFC("navigatorR1" + str(i), "Art/Interface/Screens/HomeWorld/transition_sequence/1.dds", self.XResolution / 2, self.YResolution / 2 - self.XResolution / 8, self.XResolution / 2, self.XResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				screen.hide("navigatorR1" + str(i))
			
			for i in range(9):
				screen.addDDSGFC("navigatorR2" + str(i), "Art/Interface/Screens/HomeWorld/transition_sequence/2.dds", self.XResolution / 2, self.YResolution / 2 - self.XResolution / 8, self.XResolution / 2, self.XResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				screen.hide("navigatorR2" + str(i))
			
			for i in range(15):
				screen.addDDSGFC("linerHomeworld" + str(i), "Art/Interface/Screens/HomeWorld/liner_faded.dds", self.XResolution / 4 - self.YResolution / 4 , self.YResolution / 12, self.YResolution / 2, self.YResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )
				screen.hide("linerHomeworld" + str(i))
			
			for i in range(15):
				screen.addDDSGFC("linerArrakis" + str(i), "Art/Interface/Screens/HomeWorld/liner_faded.dds", self.XResolution * 3 / 4 - self.YResolution / 4, self.YResolution / 12, self.YResolution / 2, self.YResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )
					
		self.lookAtCity(self.player.firstCity(false)[0])
				
		screen.addDDSGFC("ShadowBar1", "Art/Interface/Screens/HomeWorld/shaded.dds", self.XResolution / 2, self.YResolution - 131, self.XResolution / 2 - 210, 121, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.addDDSGFC("ShadowBar2", "Art/Interface/Screens/HomeWorld/shaded.dds", self.XResolution - 10, self.YResolution - 131, 11, 121, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		screen.addFlagWidgetGFC("Flag", self.XResolution / 25, self.YResolution - 170, 110, 400, gc.getGame().getActivePlayer(), WidgetTypes.WIDGET_GENERAL, self.CREDITS_BUTTON, -1)
		if not self.isFremen:
			screen.addDDSGFC("GuildLogo", "Art/Interface/Screens/HomeWorld/logo.dds", self.XResolution / 2 + 9, self.YResolution - 122, 103, 103, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.addDDSGFC("LaunchBox", "Art/Interface/Screens/HomeWorld/white_box.dds", self.XResolution - 220 - (self.XResolution - 220 - self.XResolution / 2 - 112) / 2 - 64, self.YResolution - 111, 172, 38, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.addDDSGFC("ExitBox", "Art/Interface/Screens/HomeWorld/white_box.dds", self.XResolution - 220 - (self.XResolution - 220 - self.XResolution / 2 - 112) / 2 - 64, self.YResolution - 61, 172, 38, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		
		screen.setTextAt( "HomeworldScreenExit", "ExitBox", u"<font=4>" + CyTranslator().getText("TXT_KEY_PEDIA_SCREEN_EXIT", ()).upper() + "</font>", CvUtil.FONT_CENTER_JUSTIFY, 56, 2, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_CLOSE_SCREEN, -1, -1 )
		screen.setActivation( "HomeworldScreenExit", ActivationTypes.ACTIVATE_MIMICPARENTFOCUS )
			
		szCiv = gc.getCivilizationInfo(self.player.getCivilizationType()).getType()
		
		if self.isFremen:
			TitleText = localText.getText("TXT_KEY_HW_TITLE_FREMEN", ()).upper()
		else:
			TitleText = localText.getText("TXT_KEY_HW_TITLE", ()).upper()
		
		TitleText = localText.changeTextColor(TitleText, gc.getInfoTypeForString("COLOR_FONT_CREAM"))
		screen.setText( "Title", "Background", u"<font=4b>" + TitleText + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, 4, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
		
		self.setGoldText(0)
				
		szMessage = localText.getText("TXT_KEY_PLANET_" + szCiv, (MercenaryUtils.dictHomeworld[szCiv].upper(), gc.getCivilizationInfo(self.player.getCivilizationType()).getDescription()))
		screen.addPanel("DescriptionPanel", "", "", true, false, self.XResolution / 25 + 119, self.YResolution - 152, self.XResolution / 25 + 119 + (self.XResolution / 2 - self.XResolution / 25 - 128) / 2, 143, PanelStyles.PANEL_STYLE_EMPTY)
		screen.attachMultilineText("DescriptionPanel", "PlanetDescription", u"<font=3b>" + szMessage + u"</font>", WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_CENTER_JUSTIFY)
		
		iPlayer = self.player.getID()		
		self.persistentMercenaries, nextIdArray, sequenceArray = objMercenaryUtils.loadMercenaryData(self.player.getID())
		self.mercenaries = {} 
		for id in self.persistentMercenaries[iPlayer]:
			self.mercenaries[id] = self.persistentMercenaries[iPlayer][id]
		
		mercData = BugData.getGameData().getTable(SD_MOD_ID)
		
		if self.isFremen:
			sequenceArray[iPlayer] = "off"
		else:
			screen.addDDSGFC("SequenceBox", "Art/Interface/Screens/HomeWorld/white_box.dds", self.XResolution - self.XResolution / 25 - 128, 4, 128, 32, WidgetTypes.WIDGET_GENERAL, -1, -1 )
			screen.setTextAt( "SequenceButton", "SequenceBox", u"<font=3>" + CyTranslator().getText("Sequence: %s1", (sequenceArray[iPlayer],())).upper() + "</font>", CvUtil.FONT_CENTER_JUSTIFY, 4, 4, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, self.SEQUENCE_BUTTON, -1 )
		
		screen.addScrollPanel("CityListPanel", u"", self.XResolution - 300, self.YResolution / 12, 300, self.YResolution * 3 / 4 - self.YResolution / 12, PanelStyles.PANEL_STYLE_EXTERNAL )
		screen.setLabelAt("CityPanelTitle", "CityListPanel", u"<font=2><color=164,164,164>" + localText.getText("TXT_KEY_HW_SELECT_CITY", ()) + u"</color></font>", CvUtil.FONT_RIGHT_JUSTIFY, 250, 0, 0, FontTypes.SMALL_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
				
		iI = 0
		(city, iter) = self.player.firstCity(false)
		while (city):
			#if city.isCapital() or city.isHasBuilding(gc.getInfoTypeForString(MercenaryUtils.NEEDED_BUILDING)):
                        iCity = city.getID()
                        
                        iI += 1
                        screen.setImageButtonAt("ButtonCityMarked" + str(iCity), "CityListPanel", "Art/Interface/Screens/HomeWorld/mark2.dds", 100, 24 * iI - 2, 260, 28, WidgetTypes.WIDGET_GENERAL, -1, -1)
                        screen.setLabelAt("City" + str(iCity), "CityListPanel", u"<font=3>" + localText.getText("%s1", (city.getName(), ())) + u"</font>", CvUtil.FONT_RIGHT_JUSTIFY, 250, 24 * iI, 0, FontTypes.SMALL_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
                        screen.setImageButtonAt("ButtonCity" + str(iCity), "CityListPanel", "", 0, 24 * iI, 260, 24, WidgetTypes.WIDGET_GENERAL, self.CITY_LIST, iCity)
                        screen.hide("ButtonCityMarked" + str(iCity))
				
			(city, iter) = self.player.nextCity(iter, false)
		
		objMercenaryUtils.saveMercenaryData(self.persistentMercenaries, nextIdArray, sequenceArray)
		
		self.drawContents()


	def getScreen(self):

		return CyGInterfaceScreen(self.SCREEN_NAME, CvScreenEnums.HOMEWORLD_ADVISOR)
		

	def drawContents(self):
	
		screen = self.getScreen()
		iPlayer = self.player.getID()
				
		screen.addPanel("UnitListPanel", "", "", false, true, 0, self.YResolution / 12 + 24, 300, self.YResolution - self.YResolution / 12 - 254, PanelStyles.PANEL_STYLE_EMPTY )
		screen.setLabel("UnitPanelTitle", "", u"<font=2><color=164,164,164>" + localText.getText("TXT_KEY_HW_SELECT_UNIT", ()) + u"</color></font>", CvUtil.FONT_LEFT_JUSTIFY, self.XResolution / 25, self.YResolution / 12, 0, FontTypes.SMALL_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
		
		self.szTable = "TradeMessagePanel"
		screen.attachTableControlGFC ("UnitListPanel", self.szTable, 3, false, true, 32, 32, TableStyles.TABLE_STYLE_ALTEMPTY)
		
		screen.setTableColumnHeader(self.szTable, 0, u"", 24 + self.XResolution / 25)
		screen.setTableColumnHeader(self.szTable, 1, u"", 48)
		screen.setTableColumnHeader(self.szTable, 2, u"", 300 - self.XResolution / 25)
		
		mPlayer = self.mercenaries
		
		if len(mPlayer) > 0:
			for iI in range(len(mPlayer)):
				id = mPlayer.keys()[len(mPlayer) - iI - 1]
				UnitInfo = gc.getUnitInfo(int(mPlayer[id]["UnitType"]))
				
				if len(mPlayer) > screen.getTableNumRows(self.szTable):
					screen.appendTableRow(self.szTable)
				
				screen.setImageButtonAt("ButtonUnitMarked" + str(id), "UnitListPanel", "Art/Interface/Screens/HomeWorld/mark.dds", -100, 24 * iI - 2, 300, 28, WidgetTypes.WIDGET_GENERAL, -1, -1)
				screen.moveToBack("ButtonUnitMarked" + str(id))
				screen.hide("ButtonUnitMarked" + str(id))
				
				# addTableCellDDS (INT iRow, INT iCol, STRING szFile, INT iX, INT iY, INT iWidth, INT iHeight, INT iGroup)
				
				szColor = u"<color=255,255,255>"
				if mPlayer[id]['Elite']:
					szColor = u"<color=240,190,0>"
					
				szUnitText = szColor + localText.getText("%s1", (UnitInfo.getDescription(),())) 
				if mPlayer[id]['Elite']:
					szUnitText = szUnitText + localText.getText(" [ICON_STAR]", ())
				szUnitText = szUnitText + u"</color>"
				
				screen.setTableText(self.szTable, 1, iI, str(mPlayer[id]["Cost"]), "", WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_RIGHT_JUSTIFY)
				screen.setTableText(self.szTable, 2, iI, szUnitText, "", WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY)
				
				screen.setImageButtonAt("ButtonUnit" + str(id), "UnitListPanel", "", 0, 24 * iI, 260, 24, WidgetTypes.WIDGET_GENERAL, self.UNIT_LIST, id)
				screen.setImageButtonAt( "UnitIcon" + str(id), "UnitListPanel", UnitInfo.getButton(), self.XResolution / 25, 24 * iI, 23, 23, WidgetTypes.WIDGET_PEDIA_JUMP_TO_UNIT, int(mPlayer[id]["UnitType"]), -1 )
				
		else:
			screen.setLabel( "EndTurnText", "Background", u"", CvUtil.FONT_CENTER_JUSTIFY, 0, self.YResolution / 2, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1 )
			screen.setHitTest( "EndTurnText", HitTestTypes.HITTEST_NOHIT )
			screen.setEndTurnState( "EndTurnText", "<font=4b>" + localText.getText("TXT_KEY_NO_REINFORCEMENT", ()) + "</font>")
			screen.hide("UnitPanelTitle")
			screen.hide("UnitListPanel")
			screen.hide("CityListPanel")
		
		if self.isFremen:
			screen.setTextAt( "TransportUnitButton", "LaunchBox", u"<font=4>" + CyTranslator().getText("TXT_KEY_HW_TRANSPORT_FREMEN", ()).upper() + "</font>", CvUtil.FONT_CENTER_JUSTIFY, 33, 2, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, self.LAUNCH_BUTTON, -1 )
		else:
			screen.setTextAt( "TransportUnitButton", "LaunchBox", u"<font=4>" + CyTranslator().getText("TXT_KEY_HW_TRANSPORT", ()).upper() + "</font>", CvUtil.FONT_CENTER_JUSTIFY, 14, 2, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, self.LAUNCH_BUTTON, -1 )
	
		return 0

	
	def handleInput(self, inputClass):
		
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_CLICKED):
									
			if (inputClass.getButtonType() == WidgetTypes.WIDGET_GENERAL):
				screen = self.getScreen()
				
				mercData = BugData.getGameData().getTable(SD_MOD_ID)
				iPlayer = self.player.getID()
				
				if (inputClass.getData1() == self.UNIT_LIST):
					id = inputClass.getData2()
					iCost =  int(self.mercenaries[id]["Cost"])
					
					if id in self.UnitList:
						screen.hide("ButtonUnitMarked" + str(id))
						self.setGoldText(-iCost)
						self.UnitList.remove(id)
				
					else:
						if iCost + self.iTotalCost <= self.iCurrentGold:
							screen.show("ButtonUnitMarked" + str(id))
							self.setGoldText(iCost)
							self.UnitList.append(id)
						else:
							screen.setSoundId(CyAudioGame().Play2DSound("AS2D_LOSS_LATE"))
							screen.show("goldMarker")
					
					szMessage = ""
					screen.setText( "LaunchButtonFeedback", "Background", u"<font=4>" + szMessage + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, self.YResolution - 150, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
						
				if (inputClass.getData1() == self.CITY_LIST):
					iCity = inputClass.getData2()
					
					if self.iSelectedCity != iCity:
						screen.hide("ButtonCityMarked" + str(self.iSelectedCity))
						screen.show("ButtonCityMarked" + str(iCity))
						
						self.lookAtCity(self.player.getCity(iCity))
						self.iSelectedCity = iCity
						self.playEffect(["EFFECT_EXPLOSION_SHOCKWAVE"])
					
					else:
						screen.hide("ButtonCityMarked" + str(iCity))
						self.iSelectedCity = -1
						
					szMessage = ""
					screen.setText( "LaunchButtonFeedback", "Background", u"<font=4>" + szMessage + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, self.YResolution - 150, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
								
				if (inputClass.getData1() == self.LAUNCH_BUTTON):
                                                                
					if self.iSelectedCity == -1:
						szMessage = localText.getText("TXT_KEY_HW_DESTINATION_NEEDED", ())
						screen.setText( "LaunchButtonFeedback", "Background", u"<font=4>" + szMessage + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, self.YResolution - 150, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
						return
					
					if len(self.UnitList) == 0:
						szMessage = localText.getText("TXT_KEY_HW_UNIT_SELECTION_NEEDED", ())
						screen.setText( "LaunchButtonFeedback", "Background", u"<font=4>" + szMessage + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2, self.YResolution - 150, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
						return
					
					# !M! -> AirUnitCapacity
                                        iUnitListAir = 0
					for i in self.UnitList:
                                                iUnitListAir += gc.getUnitInfo(self.mercenaries[i]['UnitType']).getAirUnitCap()
                                        
                                        if iUnitListAir > 0:
                                                pCity = self.player.getCity(self.iSelectedCity)
                                                iTeam = self.player.getTeam()
                                                iNumAirUnits = pCity.plot().countNumAirUnits(iTeam) + iUnitListAir
                                                if iNumAirUnits > pCity.getAirUnitCapacity(iTeam):
                                                        screen.setSoundId(CyAudioGame().Play2DSound("AS2D_LOSS_LATE"))
                                                        szMessage = localText.getText("TXT_KEY_HW_AIR_LIMIT REACHED", ())
                                                        screen.setText( "LaunchButtonFeedback", "Background", u"<font=4>" + szMessage + u"</font>", CvUtil.FONT_CENTER_JUSTIFY, self.XResolution / 2 + 107, self.YResolution - 166, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
                                                        return
						
					if self.iTotalCost > self.iCurrentGold:
						return
						
					self.iCounter = 0
					
					
					if mercData["Sequence"][iPlayer] == "on":
						self.iTransitionCity = self.iSelectedCity
						self.fTimeBackup = time.clock()
						screen.setSoundId(CyAudioGame().Play2DSound("AS2D_HWS_SEQUENCE"))
						self.bPlayTransition = true
					else:
						self.playEffect(["EFFECT_STASIS"])
					
					for id in self.UnitList:
						CyMessageControl().sendModNetMessage(690, iPlayer, self.iSelectedCity, id, -1)
						del self.mercenaries[id]
					
					self.UnitList = []
					
					self.iCurrentGold -= self.iTotalCost
					self.iTotalCost = 0
					self.setGoldText(0)
					self.drawContents()

				if (inputClass.getData1() == self.SEQUENCE_BUTTON):
					szSequence = mercData["Sequence"][iPlayer]
					
					if szSequence == "on":
						mercData["Sequence"][iPlayer] = "off"
						screen.setSoundId(CyAudioGame().Play2DSound("AS2D_LOSS_MIDDLE"))
						screen.setTextAt( "SequenceButton", "SequenceBox", u"<font=3>" + CyTranslator().getText("Sequence: off", ()).upper() + "</font>", CvUtil.FONT_CENTER_JUSTIFY, 4, 4, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, self.SEQUENCE_BUTTON, -1 )
					else:
						mercData["Sequence"][iPlayer] = "on"
						screen.setTextAt( "SequenceButton", "SequenceBox", u"<font=3>" + CyTranslator().getText("Sequence: on", ()).upper() + "</font>", CvUtil.FONT_CENTER_JUSTIFY, 4, 4, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, self.SEQUENCE_BUTTON, -1 )

					
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_CURSOR_MOVE_ON) :
			if (inputClass.getFunctionName() == "ButtonCity") :
				screen = self.getScreen()
	
				self.getScreen().show("ButtonCityMarked" + str(inputClass.getID()))
	
			#	if self.iSelectedCity != -1:
			#		return 0

			#	self.lookAtCity(self.player.getCity(inputClass.getID()))
	
			elif (inputClass.getFunctionName() == "ButtonUnit") :
				screen = self.getScreen()
				screen.show("ButtonUnitMarked" + str(inputClass.getID()))
				
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_CURSOR_MOVE_OFF) :
			if (inputClass.getFunctionName() == "ButtonCity") :
				if inputClass.getID() != self.iSelectedCity:
					self.getScreen().hide("ButtonCityMarked" + str(inputClass.getID()))

			elif (inputClass.getFunctionName() == "ButtonUnit") :	
				screen = self.getScreen()
				if not inputClass.getID() in self.UnitList:
					screen.hide("ButtonUnitMarked" + str(inputClass.getID()))
			
		return 0
		
	def update(self, fDelta):
		
		if self.bPlayTransition:
			fTimeDiff = time.clock() - self.fTimeBackup
			if fTimeDiff >= 0.03:
				self.fTimeBackup = time.clock()
				self.makeTransition(self.iCounter)
				self.iCounter += int(fTimeDiff * 3 + 1)
				#print self.iCounter
		
		return 0
	
	def makeTransition(self, iCounter):
		screen = self.getScreen()
			
		if iCounter == 0:
			for i in range(15):
				screen.hide("linerArrakis" + str(i))
				screen.hide("linerHomeworld" + str(i))
				screen.hide("navigatorR1" + str(i))
				screen.hide("navigatorR2" + str(i))
				#screen.hide("blackScreenR" + str(i))
				screen.hide("blackScreenL" + str(i))
			screen.hide("navigatorL")
		elif iCounter <= 9:
			screen.show("blackScreenR" + str(iCounter))
			screen.show("linerHomeworld" + str(iCounter))
			screen.show("navigatorR1" + str(iCounter))
		elif iCounter <= 18:
			if iCounter <= 15:
				screen.show("blackScreenR" + str(iCounter-9))
				screen.show("linerHomeworld" + str(iCounter-9))
			screen.hide("navigatorR1" + str(iCounter-9))
			screen.show("navigatorR2" + str(iCounter-9))
		elif iCounter <= 27:
			screen.hide("navigatorR2" + str(iCounter-18))
			screen.show("navigatorR1" + str(iCounter-18))
		elif iCounter <= 36:
			screen.hide("navigatorR1" + str(iCounter-27))
			screen.show("navigatorR2" + str(iCounter-27))
		elif iCounter <= 45:
			screen.hide("navigatorR2" + str(iCounter-36))
			screen.show("navigatorR1" + str(iCounter-36))
		elif iCounter <= 54:
			screen.hide("navigatorR1" + str(iCounter-45))
			screen.show("navigatorR2" + str(iCounter-45))
			if iCounter > 48:
				screen.hide("linerHomeworld" + str(iCounter-48))
		elif iCounter <= 63:
			screen.hide("navigatorR2" + str(iCounter-54))
			screen.show("navigatorR1" + str(iCounter-54))
			screen.hide("linerHomeworld" + str(iCounter-48))
		elif iCounter <= 72:
			screen.hide("navigatorR1" + str(iCounter-63))
			screen.hide("blackScreenR" + str(iCounter-63))
			screen.show("blackScreenL" + str(iCounter-63))
			screen.addDDSGFC("navigatorL", "Art/Interface/Screens/HomeWorld/transition_sequence/" + str(iCounter - 61) + ".dds", 0, self.YResolution / 2 - self.XResolution / 8, self.XResolution / 2, self.XResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		elif iCounter <= 73:
			if self.iTransitionCity == self.iSelectedCity:
				self.playEffect(["EFFECT_STASIS"])
			screen.hide("blackScreenR" + str(iCounter-63))
			screen.show("blackScreenL" + str(iCounter-63))
			screen.addDDSGFC("navigatorL", "Art/Interface/Screens/HomeWorld/transition_sequence/" + str(iCounter - 61) + ".dds", 0, self.YResolution / 2 - self.XResolution / 8, self.XResolution / 2, self.XResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )	
		elif iCounter <= 133:
			if iCounter <= 78:
				screen.hide("blackScreenR" + str(iCounter-63))
				screen.show("blackScreenL" + str(iCounter-63))
			elif 108 < iCounter < 125:
				screen.show("linerArrakis" + str(iCounter-108))
			screen.addDDSGFC("navigatorL", "Art/Interface/Screens/HomeWorld/transition_sequence/" + str(((iCounter - 62) % 12) + 13) + ".dds", 0, self.YResolution / 2 - self.XResolution / 8, self.XResolution / 2, self.XResolution / 4, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		elif iCounter <= 148:
			screen.hide("navigatorL")
			screen.hide("blackScreenL" + str(iCounter-133))
		elif iCounter >= 149:
			self.bPlayTransition = false
	
	def onClose(self) :
		
		CyInterface().setShowInterface(InterfaceVisibility.INTERFACE_SHOW)
		CyCamera().SetZoom(self.fZoom)
		
		return 0


	def playEffect(self, effects):
		if self.iSelectedCity == -1:
			return 0
				
		for sfx in effects:
			pCityPlot = self.player.getCity(self.iSelectedCity).plot()
			iSFX = gc.getInfoTypeForString(sfx)
			
			if iSFX == -1:
				return 0
						
			CyEngine().triggerEffect(iSFX, pCityPlot.getPoint())
					
		return 0
	
	def setGoldText(self, iCost):
		
		self.iTotalCost += iCost
		if self.iTotalCost > 0:
			GoldText = localText.getText("[ICON_GOLD]: %d1 (-%d2)", (self.iCurrentGold, self.iTotalCost)).upper()
		else:
			GoldText = localText.getText("[ICON_GOLD]: %d1 (%d2)", (self.iCurrentGold, self.iTotalCost)).upper()
		GoldText = localText.changeTextColor(GoldText, gc.getInfoTypeForString("COLOR_FONT_CREAM"))
		
		screen = self.getScreen()
		screen.addDDSGFC("goldMarker", "Art/Interface/Screens/HomeWorld/mark.dds", -100, 4, 300, 28, WidgetTypes.WIDGET_GENERAL, -1, -1 )
		screen.hide("goldMarker")
		screen.setLabel( "GoldText", "Background", u"<font=4b>" + GoldText + u"</font>", CvUtil.FONT_LEFT_JUSTIFY, self.XResolution / 25, 4, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
	
	
	def lookAtCity(self, pCity):

		pLookAtPlot = CyMap().plot(pCity.getX() - 2, pCity.getY() + 2)
		CyCamera().JustLookAtPlot(pLookAtPlot)
