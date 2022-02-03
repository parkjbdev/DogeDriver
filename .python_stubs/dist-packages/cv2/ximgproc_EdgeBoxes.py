# encoding: utf-8
# module cv2
# from /usr/lib/python3/dist-packages/cv2.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2 as  # <module 'cv2'>
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.aruco as aruco # <module 'cv2.aruco'>
import cv2.bgsegm as bgsegm # <module 'cv2.bgsegm'>
import cv2.bioinspired as bioinspired # <module 'cv2.bioinspired'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.datasets as datasets # <module 'cv2.datasets'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.dynafu as dynafu # <module 'cv2.dynafu'>
import cv2.face as face # <module 'cv2.face'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.freetype as freetype # <module 'cv2.freetype'>
import cv2.ft as ft # <module 'cv2.ft'>
import cv2.hdf as hdf # <module 'cv2.hdf'>
import cv2.hfs as hfs # <module 'cv2.hfs'>
import cv2.img_hash as img_hash # <module 'cv2.img_hash'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.kinfu as kinfu # <module 'cv2.kinfu'>
import cv2.line_descriptor as line_descriptor # <module 'cv2.line_descriptor'>
import cv2.linemod as linemod # <module 'cv2.linemod'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.motempl as motempl # <module 'cv2.motempl'>
import cv2.multicalib as multicalib # <module 'cv2.multicalib'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.omnidir as omnidir # <module 'cv2.omnidir'>
import cv2.optflow as optflow # <module 'cv2.optflow'>
import cv2.plot as plot # <module 'cv2.plot'>
import cv2.ppf_match_3d as ppf_match_3d # <module 'cv2.ppf_match_3d'>
import cv2.quality as quality # <module 'cv2.quality'>
import cv2.reg as reg # <module 'cv2.reg'>
import cv2.rgbd as rgbd # <module 'cv2.rgbd'>
import cv2.saliency as saliency # <module 'cv2.saliency'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.structured_light as structured_light # <module 'cv2.structured_light'>
import cv2.text as text # <module 'cv2.text'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.videostab as videostab # <module 'cv2.videostab'>
import cv2.viz as viz # <module 'cv2.viz'>
import cv2.ximgproc as ximgproc # <module 'cv2.ximgproc'>
import cv2.xphoto as xphoto # <module 'cv2.xphoto'>

from .Algorithm import Algorithm

class ximgproc_EdgeBoxes(Algorithm):
    # no doc
    def getAlpha(self): # real signature unknown; restored from __doc__
        """
        getAlpha() -> retval
        .   @brief Returns the step size of sliding window search.
        """
        pass

    def getBeta(self): # real signature unknown; restored from __doc__
        """
        getBeta() -> retval
        .   @brief Returns the nms threshold for object proposals.
        """
        pass

    def getBoundingBoxes(self, edge_map, orientation_map, scores=None): # real signature unknown; restored from __doc__
        """
        getBoundingBoxes(edge_map, orientation_map[, scores]) -> boxes, scores
        .   @brief Returns array containing proposal boxes.
        .   
        .       @param edge_map edge image.
        .       @param orientation_map orientation map.
        .       @param boxes proposal boxes.
        .       @param scores of the proposal boxes, provided a vector of float types.
        """
        pass

    def getClusterMinMag(self): # real signature unknown; restored from __doc__
        """
        getClusterMinMag() -> retval
        .   @brief Returns the cluster min magnitude.
        """
        pass

    def getEdgeMergeThr(self): # real signature unknown; restored from __doc__
        """
        getEdgeMergeThr() -> retval
        .   @brief Returns the edge merge threshold.
        """
        pass

    def getEdgeMinMag(self): # real signature unknown; restored from __doc__
        """
        getEdgeMinMag() -> retval
        .   @brief Returns the edge min magnitude.
        """
        pass

    def getEta(self): # real signature unknown; restored from __doc__
        """
        getEta() -> retval
        .   @brief Returns adaptation rate for nms threshold.
        """
        pass

    def getGamma(self): # real signature unknown; restored from __doc__
        """
        getGamma() -> retval
        .   @brief Returns the affinity sensitivity.
        """
        pass

    def getKappa(self): # real signature unknown; restored from __doc__
        """
        getKappa() -> retval
        .   @brief Returns the scale sensitivity.
        """
        pass

    def getMaxAspectRatio(self): # real signature unknown; restored from __doc__
        """
        getMaxAspectRatio() -> retval
        .   @brief Returns the max aspect ratio of boxes.
        """
        pass

    def getMaxBoxes(self): # real signature unknown; restored from __doc__
        """
        getMaxBoxes() -> retval
        .   @brief Returns the max number of boxes to detect.
        """
        pass

    def getMinBoxArea(self): # real signature unknown; restored from __doc__
        """
        getMinBoxArea() -> retval
        .   @brief Returns the minimum area of boxes.
        """
        pass

    def getMinScore(self): # real signature unknown; restored from __doc__
        """
        getMinScore() -> retval
        .   @brief Returns the min score of boxes to detect.
        """
        pass

    def setAlpha(self, value): # real signature unknown; restored from __doc__
        """
        setAlpha(value) -> None
        .   @brief Sets the step size of sliding window search.
        """
        pass

    def setBeta(self, value): # real signature unknown; restored from __doc__
        """
        setBeta(value) -> None
        .   @brief Sets the nms threshold for object proposals.
        """
        pass

    def setClusterMinMag(self, value): # real signature unknown; restored from __doc__
        """
        setClusterMinMag(value) -> None
        .   @brief Sets the cluster min magnitude.
        """
        pass

    def setEdgeMergeThr(self, value): # real signature unknown; restored from __doc__
        """
        setEdgeMergeThr(value) -> None
        .   @brief Sets the edge merge threshold.
        """
        pass

    def setEdgeMinMag(self, value): # real signature unknown; restored from __doc__
        """
        setEdgeMinMag(value) -> None
        .   @brief Sets the edge min magnitude.
        """
        pass

    def setEta(self, value): # real signature unknown; restored from __doc__
        """
        setEta(value) -> None
        .   @brief Sets the adaptation rate for nms threshold.
        """
        pass

    def setGamma(self, value): # real signature unknown; restored from __doc__
        """
        setGamma(value) -> None
        .   @brief Sets the affinity sensitivity
        """
        pass

    def setKappa(self, value): # real signature unknown; restored from __doc__
        """
        setKappa(value) -> None
        .   @brief Sets the scale sensitivity.
        """
        pass

    def setMaxAspectRatio(self, value): # real signature unknown; restored from __doc__
        """
        setMaxAspectRatio(value) -> None
        .   @brief Sets the max aspect ratio of boxes.
        """
        pass

    def setMaxBoxes(self, value): # real signature unknown; restored from __doc__
        """
        setMaxBoxes(value) -> None
        .   @brief Sets max number of boxes to detect.
        """
        pass

    def setMinBoxArea(self, value): # real signature unknown; restored from __doc__
        """
        setMinBoxArea(value) -> None
        .   @brief Sets the minimum area of boxes.
        """
        pass

    def setMinScore(self, value): # real signature unknown; restored from __doc__
        """
        setMinScore(value) -> None
        .   @brief Sets the min score of boxes to detect.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


