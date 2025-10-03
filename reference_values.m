clc; clear; close all
format long

R = 287.085;    % gas constant [J/kg*K]
gamma = 1.4;    % cp / cv
p_inf = 101325; % freestream pressure [Pa]
T_inf = 303.15; % freestream temperature [K]
U_inf = 7;      % freestream velocity [m/s]
l_ref = 14e-3;  % Re length [m]

rho_inf = p_inf / (R*T_inf) % freestream density [kg/m^3]

% sutherland law
mu_ref = 1.716e-5;
T_ref = 273.15;
S = 110.4;
mu = mu_ref * (T_inf / T_ref) ^ 1.5 * (T_ref + S) / (T_inf + S) % dynamic viscosity [Pa*s]

Ma = U_inf / sqrt(gamma*R*T_inf) % Mach number

Re = rho_inf * l_ref * U_inf / mu % Reynolds number

T_tot = T_inf * (1 + (gamma-1) / 2 * Ma^2) % total temperature [K]
p_tot = p_inf * (1 + (gamma-1) / 2 * Ma^2) ^ (gamma / (gamma-1)) % total pressure [Pa]


