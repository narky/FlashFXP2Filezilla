#!/usr/bin/env python
# -*- coding: UTF-8  -*-

# =====================================
# Filezilla.xml 文件模板
# File: Template.py
# Class: 
# =====================================

fileTemplate = """<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<FileZilla3>
    <Servers>
        %s
    </Servers>
</FileZilla3>"""

serverTemplate = """<Server>
            <Host>%s</Host>
            <Port>%s</Port>
            <Protocol>%s</Protocol>
            <Type>%s</Type>
            <User>%s</User>
            <Pass>%s</Pass>
            <Logontype>%s</Logontype>
            <TimezoneOffset>%s</TimezoneOffset>
            <PasvMode>%s</PasvMode>
            <MaximumMultipleConnections>%s</MaximumMultipleConnections>
            <EncodingType>%s</EncodingType>
            <BypassProxy>%s</BypassProxy>
            <Name>%s</Name>
            <Comments>%s</Comments>
            <LocalDir>%s</LocalDir>
            <RemoteDir>%s</RemoteDir>
            <SyncBrowsing>%s</SyncBrowsing>%s
        </Server>
        """

folderTemplate="""<Folder expanded="1">%s
            %s
        </Folder>
        """