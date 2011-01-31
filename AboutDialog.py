#!/usr/bin/env python
# -*- coding: UTF-8  -*-

__author__ = 'narky'
__date__ = '11-1-25'
__version__ = '1.0'

import wx
import wx.html
from Lang import _L

class AboutDialog ( wx.Dialog ):

	def __init__( self, parent, title ):
		wx.Dialog.__init__ ( self, parent, wx.ID_ANY, title, pos = wx.DefaultPosition, size = wx.Size( 350,280 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.aboutHtmlWin = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(350,210), wx.html.HW_SCROLLBAR_NEVER )
		bSizer4.Add( self.aboutHtmlWin, 0, wx.ALL, 0 )

		self.btnClose = wx.Button( self, wx.ID_ANY, _L["about_close"], wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnClose, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnInit )
		self.btnClose.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnInit( self, event ):
		aboutHtml = u"""
		<html>
<body bgcolor="#eff9ff" leftmargin="0" topmargin="0">
<center><table bgcolor="#fefefe" width="100%" cellspacing="0" cellpadding="0" border="0">
<tr>
    <td align="center"><h3><font color="#0066cc">FlashFXP -> FileZilla 站点转换工具</font></h3></td>
</tr>
</table>
</center>
<p>Author:<a href="mailto:narky05@gmail.com">Narky</a><br>
· Python 2.5<br>
· wxPython 2.8<br>
· GUI generated with wxFormBuilder(version Oct  4 2010)<br>
· Code with PyCharm 1.1.1<br>
</p>
</body>
</html>"""
		self.aboutHtmlWin.SetPage(aboutHtml)

	def OnClose(self, event):
		self.Destroy()

def main():
	app = wx.PySimpleApp()
	abt = AboutDialog(None,u"关于")
	abt.ShowModal()
	app.MainLoop()

if __name__=="__main__":
	main()