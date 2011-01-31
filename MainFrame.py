#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct  4 2010)
## http://www.wxformbuilder.org/
###########################################################################

import wx
import os
import locale
import Core
from Lang import _Lang

_L = _Lang[locale.getdefaultlocale()[0]]

# 拖放文件实现
class MyFileDropTarget(wx.FileDropTarget):#声明释放到的目标
	def __init__(self, window):
		wx.FileDropTarget.__init__(self)
		self.window = window

	def OnDropFiles(self, x, y, filenames):#释放文件处理函数数据
		# #self.window.AppendText("\n%d file(s) dropped at (%d,%d):\n" %(len(filenames), x, y))
		self.window.SetValue(filenames[0])

# 主要窗体
class MainFrame ( wx.Frame ):
	
	def __init__( self, parent, title ):
		wx.Frame.__init__ ( self, parent, wx.ID_ANY, title, pos = wx.DefaultPosition, size = wx.Size( 454,147 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _L["select_ftp_file"], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_LEFT|wx.LEFT|wx.TOP, 10 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtFile = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), wx.TE_READONLY )
		bSizer2.Add( self.txtFile, 0, wx.LEFT|wx.TOP, 10 )
		
		self.btnBrowser = wx.Button( self, wx.ID_ANY, _L["select"], wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer2.Add( self.btnBrowser, 0, wx.LEFT|wx.TOP, 10 )
		
		bSizer1.Add( bSizer2, 1, wx.FIXED_MINSIZE, 0 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnRun = wx.Button( self, wx.ID_ANY, _L["run"], wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnRun, 0, wx.ALL, 10 )

		bSizer3.AddSpacer( ( 156, 0), 1, wx.EXPAND, 5 )

		self.btnAbout = wx.Button(self, wx.ID_ANY, _L["about"], wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add(self.btnAbout, 0, wx.ALL, 10)
		
		self.btnExit = wx.Button( self, wx.ID_ANY, _L["exit"], wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnExit, 0, wx.ALL, 10 )
		
		bSizer1.Add( bSizer3, 1, wx.FIXED_MINSIZE, 0 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		# Lock Size
		self.btnRun.Enable(False)
		self.MaxSize = self.Size
		self.MinSize = self.Size
		
		# make the text control be a drop target
		dt = MyFileDropTarget(self.txtFile)#将文本控件作为释放到的目标
		self.txtFile.SetDropTarget(dt)
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.ConfirmExit )
		self.txtFile.Bind( wx.EVT_TEXT, self.OnTextChange )
		self.btnBrowser.Bind( wx.EVT_BUTTON, self.OnBrowser )
		self.btnRun.Bind( wx.EVT_BUTTON, self.OnRun )
		self.btnAbout.Bind( wx.EVT_BUTTON, self.OnAbout )
		self.btnExit.Bind( wx.EVT_BUTTON, self.ConfirmExit )
	
	
	# Virtual event handlers, overide them in your derived class
	def OnBrowser( self, event ):
		filedlg = wx.FileDialog(None,_L["select_file"],"",wildcard=_L["wildcard"])
		if filedlg.ShowModal()==wx.ID_OK:
			self.txtFile.SetValue(filedlg.GetPath())
	
	def OnRun( self, event ):
		filedlg = wx.FileDialog(None,_L["save_file"],defaultFile="Filezilla.xml",wildcard=_L["save_wildcard"])
		if filedlg.ShowModal() == wx.ID_OK:
			savefile = filedlg.GetPath()
			if os.path.isfile(savefile):
				if wx.MessageDialog(None,_L["file_exist_confirm_to_overwrite"],_L["warning"],wx.YES_NO|wx.ICON_WARNING).ShowModal()==wx.ID_YES:
					self.DoRun(savefile)

	def OnTextChange(self, event):
		self.btnRun.Enable(True)

	def OnAbout(self, event):
		from AboutDialog import AboutDialog
		aboutdlg = AboutDialog(None,_L["about_title"])
		aboutdlg.ShowModal()

	def ConfirmExit( self, event ):
		dlg = wx.MessageDialog(None,_L["confirm_exit"],_L["warning"],wx.YES_NO|wx.ICON_WARNING)
		if dlg.ShowModal()==wx.ID_YES:
			self.Destroy()

	def DoRun( self, savefile="FileZilla.xml"):
		if os.path.isfile(self.txtFile.GetValue()):
			r = Core.XML2Dict().parse(self.txtFile.GetValue())
			if Core.writeFilezillaXmlFile(r,savefile):
				wx.MessageBox(_L["run_complete"],_L["msg"])
			else:
				wx.MessageBox(_L["run_faild"],_L["msg"])
		else:
			wx.MessageBox(_L["file_not_exist"],_L["error"],wx.ICON_ERROR)

def main():
	app = wx.PySimpleApp()
	frm = MainFrame(None,_L["title"])
	frm.Show()
	app.MainLoop()

if __name__=='__main__':
	main()