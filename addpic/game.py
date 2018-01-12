# -*- coding: utf-8 -*-
import os
import time
import wx
import pygame
import sys
import random
from pygame.locals import *
from PIL import Image,ImageTk
import matplotlib.pyplot as plt

# 一些常量
BACKGROUNDCOLOR = (255, 255, 255)
red = (255,0,0)
BLACK = (0, 0, 0)
FPS = 40

MAXRANDTIME = 100


def startTime():
    pretime = time.localtime()
    pretime_min,pretime_sec = pretime.tm_min,pretime.tm_sec
    return pretime_min,pretime_sec

# 随机生成游戏盘面
def newGameBoard(VHNUMS,CELLNUMS):
    board = []
    for i in range(CELLNUMS):
        board.append(i)
    blackCell = CELLNUMS - 1
    board[blackCell] = -1

    for i in range(MAXRANDTIME):
        direction = random.randint(0, 3)
        if (direction == 0):
            blackCell = moveLeft(board, blackCell,VHNUMS,CELLNUMS)
        elif (direction == 1):
            blackCell = moveRight(board, blackCell,VHNUMS,CELLNUMS)
        elif (direction == 2):
            blackCell = moveUp(board, blackCell,VHNUMS,CELLNUMS)
        elif (direction == 3):
            blackCell = moveDown(board, blackCell,VHNUMS,CELLNUMS)
    return board, blackCell


# 若空白图像块不在最左边，则将空白块左边的块移动到空白块位置
def moveRight(board, blackCell,VHNUMS,CELLNUMS):
    if blackCell % VHNUMS == 0:
        return blackCell
    board[blackCell - 1], board[blackCell] = board[blackCell], board[blackCell - 1]
    return blackCell - 1


# 若空白图像块不在最右边，则将空白块右边的块移动到空白块位置
def moveLeft(board, blackCell,VHNUMS,CELLNUMS):
    if blackCell % VHNUMS == VHNUMS - 1:
        return blackCell
    board[blackCell + 1], board[blackCell] = board[blackCell], board[blackCell + 1]
    return blackCell + 1


# 若空白图像块不在最上边，则将空白块上边的块移动到空白块位置
def moveDown(board, blackCell,VHNUMS,CELLNUMS):
    if blackCell < VHNUMS:
        return blackCell
    board[blackCell - VHNUMS], board[blackCell] = board[blackCell], board[blackCell - VHNUMS]
    return blackCell - VHNUMS


# 若空白图像块不在最下边，则将空白块下边的块移动到空白块位置
def moveUp(board, blackCell,VHNUMS,CELLNUMS):
    if blackCell >= CELLNUMS - VHNUMS:
        return blackCell
    board[blackCell + VHNUMS], board[blackCell] = board[blackCell], board[blackCell + VHNUMS]
    return blackCell + VHNUMS


# 是否完成
def isFinished(board, blackCell,CELLNUMS):
    for i in range(CELLNUMS - 1):
        if board[i] != i:
            return False
    return True

def successEnd():
    wx.MessageBox("你好棒呦！","提示")

def falseEnd():
    wx.MessageBox("超时了呦！","提示")

def draw_info(surfacetodraw,minutes,seconds,font):
    surfacetodraw.fill(BACKGROUNDCOLOR)
    now = time.localtime()
    now_min,now_sec = now.tm_min,now.tm_sec
    time_passed = now_min * 60.0 + now_sec - (minutes * 60.0 + seconds)
    str_time_limit=u"限制为3min左右哦~"
    str_time_sign = u"已花费时间:"
    str_time_passed=str(time_passed) + u"秒"
    limit_surface=font.render(str_time_limit,True,red)
    sign_surface = font.render(str_time_sign,True,red)
    time_surface = font.render(str_time_passed,True,red)
    surfacetodraw.blit(limit_surface,(0,0))
    surfacetodraw.blit(sign_surface,(0,limit_surface.get_height()))
    surfacetodraw.blit(time_surface,(0,limit_surface.get_height()+sign_surface.get_height()))

def checkTime(minutes,seconds):
    now = time.localtime()
    now_min,now_sec = now.tm_min,now.tm_sec
    time_passed = now_min * 60.0 + now_sec - (minutes * 60.0 + seconds)
    if int(time_passed)>=180:
        return True
    else:
        return False

# ====================================================================================================================

# 开始游戏 函数
def startGame(newPic,VHNUMS):
    # 初始化
    pygame.init()
    pygame.mixer.init()
    mainClock = pygame.time.Clock()
    #设置图标
    icoPath = os.getcwd()+'/favicon.ico'
    icoSet = pygame.image.load(icoPath)
    pygame.display.set_icon(icoSet)

    #成功
    success = pygame.mixer.Sound(os.getcwd()+'/success.wav')
    success.set_volume(0.25)

    info_surface = pygame.Surface((300,100))
    font = pygame.font.Font(os.getcwd()+"/simsun.ttf",17)

    pretime_min,pretime_sec=startTime()

    CELLNUMS=VHNUMS*VHNUMS
    # 加载图片
    gameImage = pygame.image.load(newPic)
    gameRect = gameImage.get_rect()

    # 设置窗口
    windowSurface = pygame.display.set_mode((gameRect.width+200, gameRect.height))
    pygame.display.set_caption('拼图游戏')

    cellWidth = int(gameRect.width / VHNUMS)
    cellHeight = int(gameRect.height / VHNUMS)

    finish = False
    temp = True
    passtime=False

    gameBoard, blackCell = newGameBoard(VHNUMS,CELLNUMS)

    # 游戏主循环
    while temp:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                temp = False
            if finish:
                success.play()
                successEnd()
                terminate()
                temp = False
                finish=False
            if passtime:
                falseEnd()
                terminate()
                temp=False
                passtime=False
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    blackCell = moveLeft(gameBoard, blackCell,VHNUMS,CELLNUMS)
                if event.key == K_RIGHT or event.key == ord('d'):
                    blackCell = moveRight(gameBoard, blackCell,VHNUMS,CELLNUMS)
                if event.key == K_UP or event.key == ord('w'):
                    blackCell = moveUp(gameBoard, blackCell,VHNUMS,CELLNUMS)
                if event.key == K_DOWN or event.key == ord('s'):
                    blackCell = moveDown(gameBoard, blackCell,VHNUMS,CELLNUMS)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * VHNUMS
                if (index == blackCell - 1 or index == blackCell + 1 or index == blackCell - VHNUMS or index == blackCell + VHNUMS):
                    gameBoard[blackCell], gameBoard[index] = gameBoard[index], gameBoard[blackCell]
                    blackCell = index

        if (isFinished(gameBoard, blackCell,CELLNUMS)):
            gameBoard[blackCell] = CELLNUMS - 1
            finish = True

        if temp:
            windowSurface.fill(BACKGROUNDCOLOR)
            for i in range(CELLNUMS):
                rowDst = int(i / VHNUMS)
                colDst = int(i % VHNUMS)
                rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

                if gameBoard[i] == -1:
                    continue

                rowArea = int(gameBoard[i] / VHNUMS)
                colArea = int(gameBoard[i] % VHNUMS)
                rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
                windowSurface.blit(gameImage, rectDst, rectArea)

            for i in range(VHNUMS + 1):
                pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
            for i in range(VHNUMS + 1):
                pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))
            if checkTime(pretime_min,pretime_sec):
                passtime=True
            draw_info(info_surface,pretime_min,pretime_sec,font)
            windowSurface.blit(info_surface,(gameRect.width+40, gameRect.height/2))
            pygame.display.update()
            mainClock.tick(FPS)

# 退出
def terminate():
    pygame.quit()