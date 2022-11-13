function cmap = cmasher(ColormapName,varargin) 
% cmasher returns perceptually-uniform scientific colormaps.
% 
%% Syntax 
% 
%  cmasher 
%  cmap = cmasher('ColormapName') 
%  cmap = cmasher('-ColormapName') 
%  cmap = cmasher(...,NLevels)
%  cmap = cmasher(...,'pivot',PivotValue) 
%  cmasher(...)
% 
%% Description 
% 
% cmasher without any inputs displays the options for colormaps. 
%
% cmasher ColormapName sets the colormap of the current axis. 
% 
% cmap = cmasher('ColormapName') returns  colormap.  For a visual
% depiction of valid colormap names, type |cmasher|. 
%
% cmap = cmasher('-ColormapName') a minus sign preceeding any ColormapName flips the
% order of the colormap. 
%
% cmap = cmasher(...,NLevels) specifies a number of levels in the colormap.  Default
% value is 256. 
%
% cmap = cmasher(...,'pivot',PivotValue) centers a diverging colormap such that white 
% corresponds to a given value and maximum extents are set using current caxis limits. 
% If no PivotValue is set, 0 is assumed. 
%
% cmasher(...) without any outputs sets the current colormap to the current axes.  
% 
%% Examples 
% Here are a few examples. Start with this figure: 
% 
% figure 
% peaks
% colorbar 
% 
% cmasher eclipse % sets the colormap to eclipse
%
% cmasher('tropical',6) % sets the colormap to a six-color tropical 
% 
% cmasher('-tropical',6) % flips the six-color tropical colormap
% 
%% Author Info 
% This function was written by Chad A. Greene of NASA's Jet Propulsion
% Laboratory, November 2022. 
% 
%% Citing this colormap: 
% Please acknowledge the free use of these colormaps by citing
% 
% van der Velden, (2020). CMasher: Scientific colormaps for making accessible, 
% informative and 'cmashing' plots. Journal of Open Source Software, 5(46), 2004, 
% https://doi.org/10.21105/joss.02004
% 
% See also colormap and clim.  

%% Display colormap options: 

if nargin==0
   figure('menubar','none','numbertitle','off','Name','cmasher options:')
   
   axes('pos',[0 0 1 1])
   image(imread('cmasher/colormaps/cmap_overview_split.png')); 
   axis image off
   set(gca,'pos',[0 0 1 1])
   
   return
end

%% Error checks: 

assert(~isnumeric(ColormapName),'Input error: ColormapName must be a string.') 

%% Set defaults: 

NLevels = 256; 
autopivot = false; 
PivotValue = 0; 
InvertedColormap = false; 

%% Parse inputs: 

names = {'lavender';'dusk';'tree';'cosmic';'ember';'emerald';'lilac';'nuclear';...
   'sapphire';'toxic';'amber';'eclipse';'ghostlight';'sepia';'amethyst';'apple';...
   'arctic';'chroma';'flamingo';'freeze';'gothic';'jungle';'neutral';'rainforest';...
   'savanna';'sunburst';'swamp';'torch';'voltage';'fall';'ocean';'horizon';...
   'bubblegum';'gem';'pepper';'neon';'tropical';'iceburn';'redshift';'seaweed';...
   'watermelon';'wildfire';'guppy';'pride';'prinsenvlag';'fusion';'holly';'viola';...
   'waterlily';'infinity';'copper';'emergency';'seasons'};


% Does user want to flip the colormap direction? 
dash = strncmp(ColormapName,'-',1); 
if any(dash) 
   InvertedColormap = true; 
   ColormapName(dash) = []; 
end

% Standardize all colormap names to lowercase: 
ColormapName = lower(ColormapName); 
if strcmpi(ColormapName(end-1:end),'_s')
   error('Sorry, I know the example image shows some colormaps that end with _s, but I''m not sure if they actually exist. Try another colormap.')
end
assert(ismember(ColormapName,names),'Unrecognized colormap name. Type cmasher to see a list of available colormaps.')

% Does the user want to center a diverging colormap on a specific value? 
% This parsing support original 'zero' syntax and current 'pivot' syntax. 
tmp = strncmpi(varargin,'pivot',3); 
if any(tmp) 
   autopivot = true; 
   try
      if isscalar(varargin{find(tmp)+1})
         PivotValue = varargin{find(tmp)+1}; 
         tmp(find(tmp)+1) = 1; 
      end
   end
   varargin = varargin(~tmp); 
end

% Has user requested a specific number of levels? 
tmp = isscalar(varargin); 
if any(tmp) 
   NLevels = varargin{tmp}; 
end

%% Load RGB values and interpolate to NLevels: 

cmap = importdata(['cmasher/colormaps/',ColormapName,'/',ColormapName,'_norm.txt']);

% Interpolate if necessary: 
if NLevels~=size(cmap,1) 
   cmap = interp1(1:size(cmap,1), cmap, linspace(1,size(cmap,1),NLevels),'linear');
end

%% Invert the colormap if requested by user: 

if InvertedColormap
   cmap = flipud(cmap); 
end

%% Adjust values to current caxis limits? 

if autopivot
   clim = caxis; 
   maxval = max(abs(clim-PivotValue)); 
   cmap = interp1(linspace(-maxval,maxval,size(cmap,1))+PivotValue, cmap, linspace(clim(1),clim(2),size(cmap,1)),'linear');
end

%% Clean up 

if nargout==0
   colormap(gca,cmap) 
   clear cmap  
end
