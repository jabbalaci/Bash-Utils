#!/usr/bin/env python

#Boa:Frame:Frame1

import wx
import reddit   # sudo pip install reddit

import config as cfg


def create(parent):
    return Frame1(parent)


[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3,
 wxID_FRAME1BUTTON4, wxID_FRAME1PANEL1, wxID_FRAME1STATICLINE1,
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3,
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3,
 wxID_FRAME1TEXTCTRL4, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6,
] = [wx.NewId() for _init_ctrls in range(16)]


def get_clipboard_data():
    if not wx.TheClipboard.IsOpened():  # may crash, otherwise
        do = wx.TextDataObject()
        wx.TheClipboard.Open()
        success = wx.TheClipboard.GetData(do)
        wx.TheClipboard.Close()
        if success:
            return do.GetText()
        else:
            return ''


def submit_to_reddit(title, url, subreddit):
    r = reddit.Reddit(user_agent="submit to reddit script")
    r.login(user=cfg.USERNAME, password=cfg.PASSWORD)

    return r.submit(subreddit, url, title)


class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(597, 334), size=wx.Size(616, 601),
              style=wx.DEFAULT_FRAME_STYLE, title='submit to reddit')
        self.SetClientSize(wx.Size(616, 601))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(616, 601),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'title', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 24), size=wx.Size(47, 29), style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(32, 64), size=wx.Size(424, 27),
              style=0, value='')

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label=u'paste',
              name='button5', parent=self.panel1, pos=wx.Point(495, 64),
              size=wx.Size(85, 29), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label='clear',
              name='button6', parent=self.panel1, pos=wx.Point(495, 104),
              size=wx.Size(85, 29), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BUTTON6)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'url', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 130), size=wx.Size(32, 29), style=0)
        self.staticText2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(32, 170), size=wx.Size(424, 27),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'choose a subreddit', name='staticText3',
              parent=self.panel1, pos=wx.Point(32, 250), size=wx.Size(230, 29),
              style=0)
        self.staticText3.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(32, 290), size=wx.Size(424, 27),
              style=0, value=cfg.get_latest_subreddit())

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'paste',
              name='button1', parent=self.panel1, pos=wx.Point(495, 170),
              size=wx.Size(85, 29), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='submit',
              name='button2', parent=self.panel1, pos=wx.Point(32, 360),
              size=wx.Size(85, 29), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(32, 440), size=wx.Size(544, 136),
              style=wx.TE_MULTILINE | wx.TE_READONLY, value='')
        self.textCtrl4.SetEditable(False)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(32, 424),
              size=wx.Size(536, 2), style=0)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='clear',
              name='button3', parent=self.panel1, pos=wx.Point(495, 210),
              size=wx.Size(85, 29), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label='reset',
              name='button4', parent=self.panel1, pos=wx.Point(130, 360),
              size=wx.Size(85, 29), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.textCtrl2.SetValue(get_clipboard_data())
        event.Skip()

    def OnButton5Button(self, event):
        self.textCtrl1.SetValue(get_clipboard_data())
        event.Skip()

    def OnButton3Button(self, event):
        self.textCtrl2.SetValue('')
        event.Skip()

    def OnButton6Button(self, event):
        self.textCtrl1.SetValue('')
        event.Skip()

    def get_title(self):
        return self.textCtrl1.GetValue().strip()

    def get_url(self):
        return self.textCtrl2.GetValue().strip()

    def get_subreddit(self):
        return self.textCtrl3.GetValue().strip()

    def OnButton2Button(self, event):
        title = self.get_title()
        url = self.get_url()
        subreddit = self.get_subreddit()
        if not title or not url or not subreddit:
            self.textCtrl4.SetValue('Error: fill all fields.')
        else:
            self.textCtrl4.SetValue('submitting... (it can take some seconds)\n')
            result = submit_to_reddit(title, url, subreddit)
            self.textCtrl4.AppendText('\n')
            self.textCtrl4.AppendText(str(result) + '\n')
            cfg.set_latest_subreddit(subreddit)

        event.Skip()

    def OnButton4Button(self, event):
        self.textCtrl1.SetValue('')
        self.textCtrl2.SetValue('')
        self.textCtrl3.SetValue('')
        self.textCtrl4.SetValue('')
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
